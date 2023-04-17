# unknown-origin
## Overview
Points: 50  
Category: Forensics

## Description
We recovered this photo but cannot seem to open it. Can you let us know where the photo was taken? It might let us know where we can find the mainframe for the rogue AI.

[Photo.jpg](./Photo.jpg)

Developed by ihanna2

## Hints

1. Maybe the photo was corrupted somehow?
## Solution

The objective of this challenge is to find where the photo was taken, how you might ask? Well, every picture that has been taken has their own metadata, this metadata show everything from when, where the photo was taken, last accessed / modified and many other information that the photo originaly has or added in the future.

With that knowledge now the tool that we can use is called `exiftool`, let's just use this by `exiftool Photo.jpg` and here is the result.

```
ExifTool Version Number         : 12.57
File Name                       : Photo.jpg
Directory                       : .
File Size                       : 38 kB
File Modification Date/Time     : 2023:04:16 03:08:37+07:00
File Access Date/Time           : 2023:04:16 03:08:47+07:00
File Inode Change Date/Time     : 2023:04:16 03:08:37+07:00
File Permissions                : -rw-r--r--
Warning                         : Processing TIFF-like data after unknown 30-byte header
Exif Byte Order                 : Little-endian (Intel, II)
GPS Satellites                  : jctf{0gre$_h@ve_l@yers}
```

The flag is written in `GPS Satellites` section of the metadata.

## Flag

```jctf{0gre$_h@ve_l@yers}```                                                  