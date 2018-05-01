#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 8088

serversocket.bind((host, port))
print('Server start at port : 8088')

serversocket.listen(5)

while True:
	clientsocket,addr = serversocket.accept()

	print('Get a connection from %s' % str(addr))

	msg = 'Thank you for connecting ' + "\r\n"
	clientsocket.send(msg.encode('ascii'))
	clientsocket.close()
