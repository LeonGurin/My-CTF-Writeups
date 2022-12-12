# OX9OR2

**376 points**

_Given:_ [encrypted]() [encryption.py]()

___

The python file encrypts the flag string with a xor cipher and an unknown key.

Finding the key == finding the plaintext string.

With the help of the `assert` functions we know how to start reversing the xor.

We know that the flag starts with `SHELL{` because its already in the flag format.

Brute forcing with a loop on each letter of the encrypted string is doable with the plaintext character known and so I did just that:

```py

enc = '8~p*m~`>'

def tryXor(msg,letter,key2):
    key = 0
    while chr(ord(msg) ^ key) != letter:
        key = key+1
    print(f'key for {letter} is {chr(key)}')
    key2 = key2.join(chr(key))
    return key2

def xor(msg):
    i = 0
    key2 = ''

    key2 += tryXor(msg[i],'S',key2)
    i += 1
    key2 += tryXor(msg[i],'H',key2)
    i += 1
    key2 += tryXor(msg[i],'E',key2)
    i += 1
    key2 += tryXor(msg[i],'L',key2)
    i += 1
    key2 += tryXor(msg[i],'L',key2)
    i += 1
    key2 += tryXor(msg[i],'{',key2)

    print(f'key up till now: {key2}')
print(xor(enc))
```

I got the first 6 letters of the key which were: `XORISC`.

Well what I did next is pretty bad but I literally guessed the next 3 letters on the first try because... `xor is cool` 🤷‍♂️.

I tried to achieve my miracle with traditional means but I did not find a way other than brute forcing by hand until normal looking letters showed up, probably something to do with the title of the challenge.

So the flag is:

>SHELL{X0R_1S_R3VeR51BL3}