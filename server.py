""" A basic console based server, only used to connect clients to one another
""" 

import socket
import threading

IP = '127.0.0.1'
PORT = 4132
data = None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(5)
conn, addr = s.accept()
#print addr

def accept_msg(server):
	data = server.recv(1024)
	print data
	server.sendall(data)

t = threading.Thread(target = accept_msg, name = 'lolidk', args = (conn))

t.start()

while 1:
	if data != None:
		print data

#try:
#	data = conn.recv(1024)
#	print data
#except:
#	print 'something bad happened'
#