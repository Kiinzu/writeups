# Simon Says
`scripting` `data processing`

In this challenge when you connect ot the nc, you'll be asked to answer some question very fast to get the flag, however because I'm in Indonesia and the Challenge Server is at East US, the script I wrote need to be run several times to get the flag.

Once you connect the default string it'll give you is 
```
combine the first 3 letters of X and the last 3 letters of Y
```
Seing the pattern we can see the letters that we need to combine is at the index 6 and 13, so we just need to send the require answer.

```python
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
```

And when we run the script
```r
[+] Opening connection to challs.actf.co on port 31402: Done
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'wombat', b'with', b'the', b'last', b'3', b'letters', b'of', b'donkey']
womkey
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'fish', b'with', b'the', b'last', b'3', b'letters', b'of', b'giraffe']
fisffe
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'dog', b'with', b'the', b'last', b'3', b'letters', b'of', b'donkey']
dogkey
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'dolphin', b'with', b'the', b'last', b'3', b'letters', b'of', b'lion']
dolion
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'fish', b'with', b'the', b'last', b'3', b'letters', b'of', b'giraffe']
fisffe
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'donkey', b'with', b'the', b'last', b'3', b'letters', b'of', b'lion']
donion
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'wombat', b'with', b'the', b'last', b'3', b'letters', b'of', b'dragon']
womgon
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'donkey', b'with', b'the', b'last', b'3', b'letters', b'of', b'zebra']
donbra
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'dragon', b'with', b'the', b'last', b'3', b'letters', b'of', b'dog']
dradog
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'dolphin', b'with', b'the', b'last', b'3', b'letters', b'of', b'dolphin']
dolhin
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'lion', b'with', b'the', b'last', b'3', b'letters', b'of', b'bear']
lioear
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'dolphin', b'with', b'the', b'last', b'3', b'letters', b'of', b'giraffe']
dolffe
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'giraffe', b'with', b'the', b'last', b'3', b'letters', b'of', b'bear']
girear
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'dolphin', b'with', b'the', b'last', b'3', b'letters', b'of', b'dog']
doldog
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'lion', b'with', b'the', b'last', b'3', b'letters', b'of', b'dolphin']
liohin
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'giraffe', b'with', b'the', b'last', b'3', b'letters', b'of', b'cat']
gircat
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'donkey', b'with', b'the', b'last', b'3', b'letters', b'of', b'cat']
doncat
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'lion', b'with', b'the', b'last', b'3', b'letters', b'of', b'wombat']
liobat
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'giraffe', b'with', b'the', b'last', b'3', b'letters', b'of', b'monkey']
girkey
[b'Combine', b'the', b'first', b'3', b'letters', b'of', b'lion', b'with', b'the', b'last', b'3', b'letters', b'of', b'dolphin']
liohin
[b'actf{simon_says_you_win}']
```

We got the flag :relaxed: