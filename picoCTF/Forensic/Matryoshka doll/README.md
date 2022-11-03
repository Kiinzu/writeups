# Matryoshka doll

## Overview
Points: 30
Category: Forensics

## Description
Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this

## Hints

1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solution

1. First thing First, by the tittle we can expect this jpg to contain files inside it, so we are going to use binwalk to see if the jpg has any file inside of it.

2. We can see it has a folder "base images" with another jpg file, let's unzip it and go to the folder.

3. As we expected, after we binwalk the 2_c.jpg we can see it has another folder, we just need to do it again until there is no more folder to unzip.

4. Finaly after the 4th we got the flag.txt

## Flag

picoCTF{4cf7ac000c3fb0fa96fb92722ffb2a32}                                                     