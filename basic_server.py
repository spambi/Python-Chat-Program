import socket
ip = 'localhost'
port = 1234
BF_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))

s.listen(1)
conn, addr = s.accept()
print '{} connected'.format(addr)

while 1:
	data = conn.recv(BF_SIZE)
	if not data: break
	conn.sendall(data)
	print data
conn.close()