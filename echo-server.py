#!/user/bin/env python3

import socket
#socket type. AF_INET is the Internet address family for IPv4
HOST='127.0.0.1' #localhost
PORT=65432 #PORT TO LISTEN TO
#we use sock.SOCK_STREAM so that data transfers with TCP so the data gets delivered in it's original sequence
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn,addr = s.accept()
	with conn:
		print("Connected by",addr)
		while True:
			# Some systems may require superuser privileges if the port is < 1024.
			data = conn.recv(1024)
			if not data:
				break
			conn.sendall(data)	
