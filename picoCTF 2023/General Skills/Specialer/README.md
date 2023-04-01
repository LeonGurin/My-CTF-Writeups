# Specialer

**300 points**

Description
Reception of Special has been cool to say the least. That's why we made an exclusive version of Special, called Secure Comprehensive Interface for Affecting Linux Empirically Rad, or just 'Specialer'. With Specialer, we really tried to remove the distractions from using a shell. Yes, we took out spell checker because of everybody's complaining. But we think you will be excited about our new, reduced feature set for keeping you focused on what needs it the most. Please start an instance to test your very own copy of Specialer.
ssh -p 64145 ctf-player@saturn.picoctf.net. The password is d8819d45

*Note:* This challenge launches an instance on demand.

___

Seeing as though I have not solved (maybe yet?) `Special` this challenge was way easier (and thus the point difference bothers me).

Connecting into the shell we're not allowed a lot of things like `cat, ls...`.

My solution was as follows:

I used `pwd` which was allowed to see where I was and the path I got was `/home/ctf-player/`, cool.

Next I figured I could `cd` and I knew that if I wanted to use tab-completion but had similar results pressing tab the autocompletion will give every file with the suffix I provided, so when you try to tab complete on files/directories that start with different letters it will provide you with the contents of the folder, so:

```
Specialer$ cd
.hushlogin  .profile    abra/       ala/        sim/
```

We can cd into any directory to check out its contents in the same way.

Inside `abra/` there were two files:

```
cadabra.txt   cadaniel.txt
```

To print out the contents I used `chatGPTs` suggestion:

```bash
$ printf "%s" "$( < file.txt )"
```

which actually worked because `printf` was allowed.

Those files were a dud but inside `ala/` printing out the file `kazam.txt` gave me the flag"

> picoCTF{y0u_d0n7_4ppr3c1473_wh47_w3r3_d01ng_h3r3_c42168d9}
