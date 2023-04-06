# Nice netcat...
## Overview
Points: 15
Category: General Skills

## Description
There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 22342`, but it doesn't speak English...

## Hints

1. You can practice using netcat with this picoGym problem: `what's a netcat?`

2. You can practice reading and writing ASCII with this picoGym problem: `Let's Warm Up`

## Solution

We need to connect first to the ip and port, once you connect, it gives you a list of number.

```
112 105 99 111 67 84 70 123 103 48 48 100 95 107 49 116 
116 121 33 95 110 49 99 51 95 107 49 116 116 121 33 95 
53 102 98 53 101 53 49 100 125 10 
```

We know that the flag format always start with `'p'` and the ASCII of 'p' is 112. Therefore, we can use python to solve this challenge.

[solver.py](./solver.py)
```python
num =[112,105,99,111,67,84,70,123,103,48,48,100,95,107,49,116,116,121,33,95,110,49,99,51,95,107,49,116,116,121,33,95,53,102,98,53,101,53,49,100,125,10,]
flag = ""
for x in num:
    flag += (chr(x))
print(flag) 
```

## Flag

```picoCTF{g00d_k1tty!_n1c3_k1tty!_5fb5e51d}```                                                 
