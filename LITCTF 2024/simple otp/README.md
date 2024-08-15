# crypto/simple otp

**552 solves / 110 points**

*Auther: Stephanie*

We all know OTP is unbreakable...

*Given:* main.py

___

We're given the file:

```py
import random

encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'

random.seed(0)
key = random.randbytes(32)
```

To retrieve the plaintext we just use the file itself and xor the encoded value with the supposedly random key (the key is not random and will be the same every time because of the seed set to 0).

My solution was just xoring and printing the flag:

```py
import random

encoded_with_xor = b'\x81Nx\x9b\xea)\xe4\x11\xc5 e\xbb\xcdR\xb7\x8f:\xf8\x8bJ\x15\x0e.n\\-/4\x91\xdcN\x8a'

random.seed(0)
key = random.randbytes(32)

decoded = bytes([b ^ k for b, k in zip(encoded_with_xor, key)])

print(decoded)
```

> LITCTF{sillyOTPlol!!!!sdfsgvkhf}
