#https://realpython.com/python-sockets/
#!/user/bin/env python3
import socket

HOST="127.0.0.1"# localhost
PORT=65432

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.connect((HOST,PORT))
	s.sendall(b'Hello,World')
	data=s.recv(1024)

print("Reciedved",repr(data))	