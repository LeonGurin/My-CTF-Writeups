# Ready Gladiator 1

**200 points**

Description
Can you make a CoreWars warrior that wins?
Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 58248 < imp.red
To get the flag, you must beat the Imp at least once out of the many rounds.

*Note:* This challenge launches an instance on demand.

___

I tried asking `chatGPT` to help me understand the syntax and what to do, but it gave me 3 programs that just lost with a weird syntax.

So the next thing I did is google, a reddit thread where someone asks how to beat the Imp gave the instructions:

```
sub 1, -10
jmp -1
```

and this code won 40 out of a 100 wins and got me the flag (still don't understand the game mostly...)

> picoCTF{1mp_1n_7h3_cr055h41r5_dba6f40d}
