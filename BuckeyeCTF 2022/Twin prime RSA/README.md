# Twin prime RSA

**100 points**

Real winners use twin primes

*Given:* [chall.py](https://github.com/LeonGurin/BuckeyeCTF-2022/blob/main/Twin%20prime%20RSA/chall.py)

___

In this RSA challenge the gimmick is that the 2 chosen prime numbers are:

```python
    p = cun.getPrime(1024)
    q = p + 2
```

and of course we could exploit it.

If `p` was equal to `q` we could just take the square root of `n` and plug everything in an RSA calculator and be done, and so that's what I basically did with 2 iterations of trial and error.

I found some `StackOverflow` code for square root of large number and copied it.

*Note:* people said that the function was not spot on because it converted to integers, so I tried multiplying:

* `(p+1) * (p+1) == n`
* `p * (p+2) == n`

and as it turned out the second iteration worked.

```python
import math

_1_50 = 1 << 50  # 2**50 == 1,125,899,906,842,624

def isqrt(x):
    """Return the integer part of the square root of x, even for very
    large integer values."""
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    if x < _1_50:
        return int(math.sqrt(x))  # use math's sqrt() for small parameters
    n = int(x)
    if n <= 1:
        return n  # handle sqrt(0)==0, sqrt(1)==1
    # Make a high initial estimate of the result (a little lower is slower!!!)
    r = 1 << ((n.bit_length() + 1) >> 1)
    while True:
        newr = (r + n // r) >> 1  # next estimate by Newton-Raphson
        if newr >= r:
            return r
        r = newr

n = 20533399299284046407152274475522745923283591903629216665466681244661861027880216166964852978814704027358924774069979198482663918558879261797088553574047636844159464121768608175714873124295229878522675023466237857225661926774702979798551750309684476976554834230347142759081215035149669103794924363457550850440361924025082209825719098354441551136155027595133340008342692528728873735431246211817473149248612211855694673577982306745037500773163685214470693140137016315200758901157509673924502424670615994172505880392905070519517106559166983348001234935249845356370668287645995124995860261320985775368962065090997084944099

p = isqrt(n)
print(p)
print()
print(p+2)
print()
print((p+2) * (p-0) == n)
```

Plugging into dcode.fr's RSA calculator we get:

>buckeye{B3_TH3R3_OR_B3_SQU4R3__abcdefghijklmonpqrstuvwxyz__0123456789}
