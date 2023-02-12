# rev/caterpillar

**200 points**

-~-~-~-~[]? -~-~-~-~[].

[caterpillar.js](https://github.com/LeonGurin/LA-CTF-2023/blob/main/caterpillar/caterpillar.js)

___

This question is all about deobfuscating javascript garbage.

The sequence of `-~` with `[]` at the end can give us numbers which in the case of the given file will be translated to values and indexes in the array.

Working through deobfuscating the whole file gives us clear cut indexes and values which should be compared to give the right output.

It should look something like this:

```javascript
const flag = "lactf{XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX}";
if (
    flag.charCodeAt(0)  == 108 && 
    flag.charCodeAt(1)  == 97 && 
    flag.charCodeAt(2)  == 99 && 
    flag.charCodeAt(3)  == 116 && 
    flag.charCodeAt(4)  == 102 && 
    flag.charCodeAt(5)  == 123 &&
    flag.charCodeAt(6)  == 116 && 
    flag.charCodeAt(7)  == 104 && 
    flag.charCodeAt(8)  == 51 && 
    flag.charCodeAt(9)  == 95 && 
    flag.charCodeAt(10) == 104 && 
    flag.charCodeAt(11) == 117 && 
    flag.charCodeAt(12) == 110 && 
    flag.charCodeAt(13) == 103 && 
    flag.charCodeAt(14) == 114 && 
    flag.charCodeAt(15) == 121 && 
    flag.charCodeAt(16) == 95 && 
    flag.charCodeAt(17) == 108 && 
    flag.charCodeAt(18) == 49 && 
    flag.charCodeAt(19) == 116 && 
    flag.charCodeAt(20) == 116 && 
    flag.charCodeAt(21) == 108 && 
    flag.charCodeAt(22) == 51 && 
    flag.charCodeAt(23) == 95 && 
    flag.charCodeAt(24) == 99 && 
    flag.charCodeAt(25) == 52 && 
    flag.charCodeAt(26) == 116 && 
    flag.charCodeAt(27) == 51 && 
    flag.charCodeAt(28) == 114 && 
    flag.charCodeAt(29) == 112 && 
    flag.charCodeAt(30) == 49 && 
    flag.charCodeAt(31) == 108 && 
    flag.charCodeAt(32) == 108 && 
    flag.charCodeAt(33) == 52 && 
    flag.charCodeAt(34) == 114 && 
    flag.charCodeAt(35) == 95 && 
    flag.charCodeAt(36) == 97 && 
    flag.charCodeAt(37) == 116 && 
    flag.charCodeAt(38) == 51 && 
    flag.charCodeAt(39) == 95 && 
    flag.charCodeAt(40) == 116 && 
    flag.charCodeAt(41) == 104 && 
    flag.charCodeAt(42) == 51 && 
    flag.charCodeAt(43) == 95 && 
    flag.charCodeAt(44) == 102 && 
    flag.charCodeAt(45) == 108 && 
    flag.charCodeAt(46) == 52 && 
    flag.charCodeAt(47) == 103 && 
    flag.charCodeAt(48) == 95 && 
    flag.charCodeAt(49) == 52 && 
    flag.charCodeAt(50) == 103 && 
    flag.charCodeAt(51) == 52 && 
    flag.charCodeAt(52) == 49 && 
    flag.charCodeAt(53) == 110 && 
    flag.charCodeAt(54) == 125 ) {
    console.log("That is the flag!");
} else {
    console.log("That is not the flag!");
}
```

We could then copy the values that are compared to and translate them to ascii to get the flag:

> lactf{th3_hungry_l1ttl3_c4t3rp1ll4r_at3_th3_fl4g_4g41n}


