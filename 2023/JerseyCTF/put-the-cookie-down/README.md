# put-the-cookie-down
## Overview
Points: 50  
Category: Web Exploitation

## Description
The Terminator has sent you a frantic message from 1996, maybe it's something important! Wait... do I smell cookies?
Flag format: jctf{string}
Developed by [Sam](https://github.com/samitman/)

https://jerseyctf-put-the-cookie-down.chals.io

## Hints

1. There is far more to Chrome DevTools than Inspect Element, what else can you find in there?

## Solution

This Challenge is pretty straight forward for me, we just need to use our Developer tools (F12) and simply go to `Application -> Cookies` and we got the string

```I_WILL_BE_BACK_FOR_MORE_C00KI3S!```

wrap the string we found using the `jctf{string}` format and we got the flag.

## Flag

```jctf{I_WILL_BE_BACK_FOR_MORE_C00KI3S!}```