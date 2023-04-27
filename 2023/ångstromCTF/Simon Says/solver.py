from pwn import *

p = remote('challs.actf.co',31402)

for x in range(100):
        q = p.recv().strip().split(b' ')
        print(q)
        first = str(q[6][:3], 'utf-8')
        second = str(q[13][-3:], 'utf-8')
        answer = first + second
        print(answer)
        p.sendline(answer.encode())