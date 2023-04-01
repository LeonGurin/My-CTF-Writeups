# Special

**300 points**

AUTHOR: LT 'SYREAL' JONES

Description
Don't power users get tired of making spelling mistakes in the shell? Not anymore! Enter Special, the Spell Checked Interface for Affecting Linux. Now, every word is properly spelled and capitalized... automatically and behind-the-scenes! Be the first to test Special in beta, and feel free to tell us all about how Special streamlines every development process that you face. When your co-workers see your amazing shell interface, just tell them: That's Special (TM)
Start your instance to see connection details.
ssh -p 49562 ctf-player@saturn.picoctf.net
The password is 483e80d4

*Note:* This challenge launches an instance on demand.

___

This was a very, very hard challenge for me.

This challenge had a lot going on, first, you couldn't enter slashes at the beginning, or type the word shell or use `:set` --> the easy options out.

What could you do?

If you typed your commands using the `$()` syntax, they would work... kinda... sometimes...

Using `$(ls)` it gave the error: `sh: 1: blargh: not found` and that means theres something called `blargh` in the directory.

It was very troublesome to perform anything on it because the autocorrect would kick in.

After many days (literal days) I figured out that I could split my commands in one line and prevent the capitaliazation of commands like `cat`.

I noticed that the command `$(echo)` worked and did nothing so I used it to eat up the capitalization at the start and in the same line used cat normally on the blargh directory.

For some reason, the autocorrect, the `/` checker did not work if I just split the commands with `;` so the final code to get the flag was:

```bash
$(echo); cat /blargh/*
```

which gave the flag:

> picoCTF{5p311ch3ck_15_7h3_w0r57_b741d1b1}
