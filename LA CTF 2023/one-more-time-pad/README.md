# crypto/one-more-time-pad

**154 points**

I heard the onetime pad is perfectly secure so I used it to send an important message to a friend, but now a UCLA competition is asking for the key? I threw that out a long time ago! Can you help me recover it?

*Given:* [chall.py](https://github.com/LeonGurin/LA-CTF-2023/blob/main/one-more-time-pad/chall.py)

___
We are given the following program:

```python
from itertools import cycle
pt = b"Long ago, the four nations lived together in harmony ..."

key = cycle(b"lactf{??????????????}")

ct = ""

for i in range(len(pt)):
    b = (pt[i] ^ next(key))
    ct += f'{b:02x}'
print("ct =", ct)

#ct = 200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e
```

Let's explain it.

The file encrypts some plaintext given in `pt` with the flag as a key using `XOR` with every byte. 

Because we are given the `ciphertext` of the resulting encryption we could simply `XOR` the `ciphertext` again with the plaintext to get the key.

Because the key is shorter than the `plaintext` they used `cycle` to make it so the key would match the length of the `plaintext` and so we`ll end up getting the relevant flag concatenated with itself but not fully like so:

`lactf{b4by_h1t_m3_0ne_m0r3_t1m3}lactf{b4by_h1t_m3_0ne_m0`

The code I used is the following:

```python
from itertools import cycle
pt = b"Long ago, the four nations lived together in harmony ..."

# key = cycle(b"lactf{??????????????}")

ct = "200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e"

# convert ct to bytes
ct = bytes.fromhex(ct)
ret = ""

for i in range(len(pt)):
    b = (pt[i] ^ ct[i])
    ret += hex(b)[2:]

print(bytes.fromhex(ret))
```

> lactf{b4by_h1t_m3_0ne_m0r3_t1m3}