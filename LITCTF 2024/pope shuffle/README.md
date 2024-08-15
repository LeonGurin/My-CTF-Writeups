# crypto/pope shuffle

**262 solves / 121 points**

*Auther: halp*

it's like caesar cipher but better. Encoded: ࠴࠱࠼ࠫ࠼࠮ࡣࡋࡍࠨ࡛ࡍ࡚ࡇ࡛ࠩࡔࡉࡌࡥ

___

A unique challenge, just giving out unprintable characters is something I've never seen before.

The way I solved it was quite random, I searched for ways to decode unprintable characters and came across a website that prints the unicode for them called [unicode-inspector](https://bobpritchett.com/unicode-inspector).

With this I extracted the escaped characters

```
\u0834\u0831\u083c\u082b\u083c\u082e\u0863\u084b\u084d\u0828\u085b\u084d\u085a\u0847\u085b\u0829\u0854\u0849\u084c\u0865
```

And plopped it inside [decode.fr/ascii-shift-cipher](https://www.dcode.fr/ascii-shift-cipher) and got the flag:

> LITCTF{ce@ser_sAlad}

