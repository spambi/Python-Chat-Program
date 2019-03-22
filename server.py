""" A basic console based server, only used to connect clients to one another
""" 

import socket

IP = '127.0.0.1'
PORT = 4132

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(1)
conn, addr = s.accept()
print '%s: Connected' % addr
fuck = conn.recv(1024)
print fuck