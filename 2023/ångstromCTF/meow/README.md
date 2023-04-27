# Meow
`netcat`
<br>
<br>

This is suppose to be the easiest challenge in this CTF, but because I live in Indonesia and the server is in East USA, I was forced to finish this with google colab.

So here is the python script I use to connect to the nc.

**conn.py**
```python
import socket

host = 'challs.actf.co'
port = 31337
s = socket.socket()
s.connect((host, port))

response = s.recv(1024)
print(response.decode())

s.close()
```

And this is the flag.

```
actf{me0w_m3ow_welcome_to_angstr0mctf}
```