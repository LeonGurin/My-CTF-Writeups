# Ready Gladiator 2

**400 points**

Description
Can you make a CoreWars warrior that wins every single round?
Your opponent is the Imp. The source is available here. If you wanted to pit the Imp against himself, you could download the Imp and connect to the CoreWars server like this:
nc saturn.picoctf.net 59243 < imp.red
To get the flag, you must beat the Imp all 100 rounds.

*Note:* This challenge launches an instance on demand.

___

So this is the final challenge in the series, we need to find the ultimate strategy to defeat the imp once and for all and constantly.

After numerous google searches I stumbled upon this reddit [thread](https://www.reddit.com/r/corewar/comments/11ulbs0/defeat_classic_imp/) and yeah, one of the comments literally says "Good luck in picoCTF23".

So google searching for the answer brought me to [link](https://everything2.com/title/corewars+imp) which states:

```
The best passive defense against an imp is known as an imp-gate. The imp-gate is an instruction that decrements some static location prior to the first code instruction of the warrior. E.g:

warrior          ; some attack code here
jmp warrior,<-10 ; decrement relative position -10
```

copying the code and sending it to the server wins the game and get us:

> picoCTF{d3m0n_3xpung3r_106bc275}
