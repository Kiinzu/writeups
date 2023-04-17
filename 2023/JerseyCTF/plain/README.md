# plain
## Overview
Points: 50  
Category: Reverse Engineering

## Description
Just a plain, simple flag checking program.

Developed by [Rajat Patel](https://github.com/PAndaContron)

## Hints

1. Don't overcomplicate things; you might not even need to run the program

## Solution

As the hint says, we don't need to overcomplicate things and not even need to run the program, so I did just that, using IDA PRO I decompile the binary and found the flag in hex-view.
```
01 00 02 00 6A 63 74 66  7B 69 5F 3C 33 5F 35 74 ....jctf{i_<3_5t
72 31 4E 67 35 5F 35 39  61 66 30 63 30 65 64 7D r1Ng5_59af0c0ed}
00 43 6F 72 72 65 63 74  21 00 00 00 01 1B 03 3B .Correct!......;
```
If you wonder what's the value of the flag, just simply search for `7D` since that is the hex value for `}` and `6A` is the hex value for `j`  

## Flag

```jctf{i_<3_5tr1Ng5_59af0c0ed}```