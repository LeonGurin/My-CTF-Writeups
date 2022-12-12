# megaxord

**60 points**

Some pesky wizard stole the article I was writing. I got it back, but it's all messed up now :(

Hint: the wizard used the same magic on every character...

*Given:* [megaxord.txt](https://github.com/LeonGurin/BuckeyeCTF-2022/blob/main/megaxord/megaxord.txt)

___

Given from the name of the challenge and the hint, we need to xor each letter until it makes sense which a key.

I made a loop that goes from 0 to 255 because its the valid numbers for the ascii tables that we could xor with and looped the whole text with all of them storing the output in a text file and then I just `Ctrl+F` to find the string `buckeye{` and found the flag.

My code:

```python
with open('megaxord.txt', 'r') as f:
    enc = f.read()

with open('megaxord_dec.txt', 'w') as g:
    i=0
    while i<256:
        for letter in enc:
            try:
                g.write(chr(ord(letter) ^ i))
            except:
                g.write('\n\n')
        i += 1
```

>buckeye{m1gh7y_m0rph1n_w1k1p3d14_p4g3}
