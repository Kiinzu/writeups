# ranch
`modified caesar cipher`

In this challenge like how a classic cryptography challenge we got a file that encrypt the flag string

**ranch.py**
```python
import string

f = open("flag.txt").read()

encrypted = "rtkw{cf0bj_czbv_nv'cc_y4mv_kf_kip_re0kyvi_uivjj1ex_5vw89s3r44901831}

"

shift = int(open("secret_shift.txt").read().strip())

for i in f:
    if i in string.ascii_lowercase:
        encrypted += chr(((ord(i) - 97 + shift) % 26)+97)
    else:
        encrypted += i

print(encrypted)
```

Based on this encryption we need to find the value of `shift` first, after that we can run this encryption again to decrypt the flag, and here is the final python that I made.

**solver.py**
```python
import string

flag = "rtkw{cf0bj_czbv_nv'cc_y4mv_kf_kip_re0kyvi_uivjj1ex_5vw89s3r44901831}"
f = "r"
encrypted = ""
# shift = int(open("secret_shift.txt").read().strip())

for i in f:
  if i in string.ascii_lowercase:
    for num in range (1,100):
      result = chr(((ord(i) - 97 + num) % 26)+97)
      if result == "a":
        shift = num

for i in flag:
    if i in string.ascii_lowercase:
        encrypted += chr(((ord(i) - 97 + shift) % 26)+97)
    else:
        encrypted += i

print(encrypted)
```

And we got the flag 

```
actf{lo0ks_like_we'll_h4ve_to_try_an0ther_dress1ng_5ef89b3a44901831}
```
