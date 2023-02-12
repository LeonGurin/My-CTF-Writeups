# rev/string-cheese

**112 points**

I'm something of a cheese connoisseur myself. If you can guess my favorite flavor of string cheese, I'll even give you a flag. Of course, since I'm lazy and socially inept, I slapped together a program to do the verification for me.

Connect to my service at `nc lac.tf 31131`

Note: The attached binary is the exact same as the one executing on the remote server.

*Given:* [string_cheese](https://github.com/LeonGurin/LA-CTF-2023/blob/main/string-cheese/string_cheese)

___

When we run the program we are asked `What's my favorite flavor of string cheese?` and we need to provide an answer to the prompt.

Because the title suggests us to use `strings` we will do just that and what do you know, in between the hard coded texts we can see a fruit:

```
flag.txt
Cannot read flag.txt.
What's my favorite flavor of string cheese?
blueberry
...how did you know? That isn't even a real flavor...
Well I guess I should give you the flag now...
Hmm... I don't think that's quite it. Better luck next time!
```

We enter blueberry and get the flag:
> lactf{d0n7_m4k3_fun_0f_my_t4st3_1n_ch33s3}



