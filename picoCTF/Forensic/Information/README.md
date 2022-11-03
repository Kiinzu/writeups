# Information

## Overview
Points: 10
Category: Forensics

## Description
Files can alway be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

## Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

## Solution

1. After we Downloaded the file, we can check by opening the file and it's a normal Cat Picture

2. I was thinking it may be hidden in the metadata, so I use exiftool to look the metadata.

3. This string `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` might be a base64 text, we can try decode it using 
```echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d ```

4. Voila we got the flag.
## Flag

picoCTF{the_m3tadata_1s_modified}