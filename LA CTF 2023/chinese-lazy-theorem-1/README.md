# crypto/chinese-lazy-theorem-1

**238 points**

I heard about this cool theorem called the Chinese Remainder Theorem, but, uh... I'm feeling kinda tired right now.

`nc lac.tf 31110`

[chinese-lazy-theorem-1.py](https://github.com/LeonGurin/LA-CTF-2023/blob/main/chinese-lazy-theorem-1/chinese-lazy-theorem-1.py)

___

The program let's the user enter a modulus number such that the printed output is the result of `print(target%modulus)` and based on that we need to guess a number between `1` and `n=p*q`.

We can get a simple solution by giving the program a modulus equal to `n` because a number modulo a number greater than itself is the number, in other words:

`target % n = target`

and so when the program starts and we receive `p` and `q` we can calculate the value of `n` and provide it to get the right guess.

When done correctly we get the flag:

> lactf{too_lazy_to_bound_the_modulus}

