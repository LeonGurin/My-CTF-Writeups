# WhatsThePerc

**50 points**

You are too drunk, you shouldn't be giving so many hints

Author: @diegosona

nc hctf.hackappatoi.com 9001

___

First I tried inputting random characters and I got the response `0.0`, I then tried to input the start of the flag format: `HCTF` and got a slightly higher value returned.

I figured that if I were to enter `HCTF{` the value will increase and for any other symbol it will stay the same.

After a few manual iterations I concluded so and wrote a python script to automatically bruteforce my way into getting the right letters by repeatedly connecting to the server and entering the current successful string with a new letter and seeing it the value returned increased:

```py
from pwn import *

enc = 'HCTF{'
val = 0.14705882352941177
letter = 0

pause = True

while pause:
    io = remote('hctf.hackappatoi.com', 9001)
    cont = io.recvuntil('\n')
    io.sendline(enc + chr(letter))
    val2 = float(io.recvuntil('\n'))
    print(f'GOT: {val2}, index: {letter}')
    if val2 == 1.0:
        print(enc)
        pause = False
    elif val2 > val:
        enc += chr(letter)
        print(enc)
        val = val2
        letter = 33
    else:
        letter += 1
```

after bruteforcing for a while (it took some time) I got the following flag

>HCTF{wh4t5_yo0r_4lch0l_p3rc3nt4g3}

