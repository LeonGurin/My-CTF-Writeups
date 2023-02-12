# crypto/guess-the-bit!

**341 points**

I'm trying out for this new game show, but it doesn't seem that hard since there are only two choices? Regardless, I heard someone name Pollard could help me out with it?

`nc lac.tf 31190`

*Given:* [chall.py](https://github.com/LeonGurin/LA-CTF-2023/blob/main/guess-the-bit!/chall.py)

___

Here is the questions code:

```python
#!/usr/local/bin/python3

import random
from Crypto.Util.number import getPrime

n = 43799663339063312211273714468571591746940179019655418145595314556164983756585900662541462573429625012257141409310387298658375836921310691578072985664621716240663221443527506757539532339372290041884633435626429390371850645743643273836882575180662344402698999778971350763364891217650903860191529913028504029597794358613653479290767790778510701279503128925407744958108039428298936189375732992781717888915493080336718221632665984609704015735266455668556495869437668868103607888809570667555794011994982530936046877122373871458757189204379101886886020141036227219889443327932080080504040633414853351599120601270071913534530651

a = 6

print("n = ", n)
print("a = ", 6)

for i in range(150):
    bit = random.randrange(0,2)
    c = random.randrange(0, n)
    c = c**2
    if bit == 1:
        c *= a
    print("c = ", c)
    guess = int(input("What is your guess? "))
    if guess != bit:
        print("Better luck next time!")
        exit()


print("Congrats! Here's your flag: ")
flag = open("flag.txt", "r").readline().strip()
print(flag)
exit(0)
```

It asks us on differently generated numbers to guess whether we the original number `c` was multiplied by `6`.

Also the number `c` is always a perfect square even before the multiplication.

We can answer all the queries given with a remote connection using `pwntools` library.

To guess whether the number has been modified we could check if its a perfect square, if so, then the number was not modified because if it was, it would be a perfect number multiplied by 6 which would not result in a perfect square.

So the only check we need to perform is a fast check to check if the number is perfect and one built in way to do it is using `gmpy2` library:

```python
from pwn import *
import gmpy2

io = remote('lac.tf', 31190)

io.recvuntil('n =  ')
n = int(io.recvline().strip())

io.recvuntil('a =  ')
a = int(io.recvline().strip())

for i in range(150):
    io.recvuntil('c =  ')
    c = int(io.recvline().strip())
    if gmpy2.is_square(c):
        print(f'SENT: {0}')
        io.sendline(b'0')
    else:
        print(f'SENT: {1}')
        io.sendline(b'1')
    
print(io.recvline().strip())
print(io.recvline().strip())
io.close()
```

And the flag we get is:

> lactf{sm4ll_pla1nt3xt_sp4ac3s_ar3n't_al4ways_e4sy}



