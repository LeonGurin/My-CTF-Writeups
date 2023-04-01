# useless

**100 points**

AUTHOR: LOIC SHEMA

Description
There's an interesting script in the user's home directory
The work computer is running SSH. We've been given a script which performs some basic calculations, explore the script and find a flag.
Hostname: saturn.picoctf.net
Port:     60547
Username: picoplayer
Password: password

*Note:* This challenge launches an instance on demand.

___

That was a tricky challenge, in the home directory there is a file named `useless` that does command line arithmetic, spoiler, it does nothing.

The interesting thing to notice was the code itself, specifically the line:

```bash
else
    echo "Read the manual"
```

Using `man` on the script we get the flag hidden at the bottom of the page.

> picoCTF{us3l3ss_ch4ll3ng3_3xpl0it3d_7065}

I personally thought it had something to do with the `challenge` directory which was inaccessible, and I thought of privilege escalation things I could do, but alas, nope.
