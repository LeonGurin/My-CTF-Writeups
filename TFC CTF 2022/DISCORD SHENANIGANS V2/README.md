**DISCORD SHENANIGANS V2 50 points**

We know that our Discord flags are the most specials ones. They raise our status! We plan to keep this tradition going, no matter what!

This one is hidden in plain s̷̤̎i̷̡͝g̴̤̿ḧ̴͚́ṫ̵̹.

Note: |̸̥͔͚͕̟̔̓̚|̴̨̫̿̎|̷͈̓̌̈|̷̼̱̦̲͐́́|̷̧͍̥͚̈̅͜͝|̷̱̱̭̏̓̈́̍̚|̴̨͚̫͇̽̌̽̕͝|̸͚̏|̴̨̬͉͔̩̈́̉͆̂͋|̸̟͇̈̾͝|̸̱͇̔̓ might be able to help you... if you ask nicely. He's a bit shy, though.

Hint: Read the message he gives you when you ask nicely very carefully!
Hint2: The flag is in #announcements
___

I actually got confused about this and the hints given.

Following the second hint I scrolled up all the messeages in `#announcements` until I saw the @ mention about the CTF.

With it came attached a picture `CURRENT STATUS`:

![img](https://github.com/LeonGurin/TFC-CTF-2022-Writeup/blob/main/DISCORD%20SHENANIGANS%20V2/current-50.png)

downloading it and using `exiftool` gives us the flag in one of its fields:

```
ExifTool Version Number         : 11.88
File Name                       : current-50.png
Directory                       : .
File Size                       : 5.7 kB
File Modification Date/Time     : 2022:07:30 22:38:30+03:00
File Access Date/Time           : 2022:07:31 01:37:57+03:00
File Inode Change Date/Time     : 2022:07:31 01:37:57+03:00
File Permissions                : rwxrwxrwx
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 480
Image Height                    : 295
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
SRGB Rendering                  : Perceptual
Author                          : TFCCTF{h1dd3n_1n_pl4in_br3ad!...1_m3an_s1gh7}
Image Size                      : 480x295
Megapixels                      : 0.142
```

So the flag is:
>TFCCTF{h1dd3n_1n_pl4in_br3ad!...1_m3an_s1gh7}

I really didn't understand it becuase there was a Bot that responded to `/flag` and when `dm`'ed got another response, but alas it wasn't even the bot...

Really confusing...