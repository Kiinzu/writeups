import socket

host = 'challs.actf.co'
port = 31337
s = socket.socket()
s.connect((host, port))

response = s.recv(1024)
print(response.decode())

s.close()