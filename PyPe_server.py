import socket
import threading

clients = {}
addresses = {}

IP = 'localhost'
PORT = 1234
BF_SIZE = 2048
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))

def accept_incoming_connections():
    """Sets up handling for incoming clients."""
    while True:
        client, client_address = s.accept()
        print("%s:%s has connected." % client_address)
        addresses[client] = client_address
        threading.Thread(target=handle_client, args=(client,)).start()

def handle_client(clientSocket):  # Takes client socket as argument.
    """Handles a single client connection."""

    username = clientSocket.recv(BF_SIZE)
    welcome = 'Welcome %s! If you ever want to quit, type {quit} to exit.' % username
    clientSocket.send(welcome)
    print 'Sent {} to {}'.format(welcome, clientSocket)
    msg = "{} has joined the chat!".format(username)
    broadcast(msg)
    clients[clientSocket] = username
    while True:
        msg = clientSocket.recv(BF_SIZE)
        print msg
        if msg != "{quit}":
            broadcast(username + ": " + msg)
        else:
            clientSocket.send("{quit}")
            clientSocket.close()
            del clients[clientSocket]
            broadcast("{} has left the chat.".format(username))
            break

def broadcast(msg, prefix=""):  # prefix is for name identification.
    """Broadcasts a message to all the clients."""
    for sock in clients:
        sock.send(prefix + msg)
        print 'Sent {} to {}'.format(msg, sock)

if __name__ == "__main__":
    s.listen(10)  # Listens for 10 connections at max.
    print("Waiting for connection...")
    ACCEPT_THREAD = threading.Thread(target=accept_incoming_connections)
    ACCEPT_THREAD.start()  # Starts the infinite loop.
    ACCEPT_THREAD.join()
    s.close()