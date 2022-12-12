# Hidden File

**397 points**

Our Agent gave us this image can you find whats there with this image?

_Given:_ [Hidden.jpg](https://github.com/LeonGurin/Shell-CTF-2022/blob/main/Hidden%20File/Hidden.jpg)

___

The hint states `can you find whats there *with* this image?` which can be interpreted as, "there is something within the image".

The tool `steghide` is used to hide files in images and could be extracted with a password.

Time to find the password, for that I ran `exiftool` and we can clearly see:

```
Make                            : the password is shell;
Artist                          : the password is shell
XP Author                       : the password is shell
```

and if we run `steghide extract -sf Hidden.jpg`
and enter the password: `shell`, we can extract new files:

* Hidden Files.zip (this is just the zip of all the other files extracted)
* flag.zip
* se3cretf1l3.pdf
* something.jpg

Starting off the `something.jpg` image was a `QR CODE` and when scanned brought you to a `sussy video`. I could'nt find anything else about the file using other forensics tools.

Moving on, the pdf had the lyrics to the `sussy video` in the QR code. 

**BUT**, I did notice that there were extra lines to the file which where "empty".

Copying all the contents of the file with `Ctrl+A` and pasting to a text file I saw:

```
Never gonna give you up 
Never gonna let you down 
Never gonna run around and desert you 
Never gonna make you cry 
Never gonna say goodbye 
Never gonna tell a lie and hurt you 
key is shellctf 
```

Aha! new key.

Finally, after trying to unzip the `flag.zip` file with `unzip` and it failing I used trusty old `WinRAR` and it prompted for a password...

hmmm, where did we get a key? that's right, the key was `shellctf`.

Providing it to WinRAR got us a new file named `flag.txt` which had the flag:

>shell{y0u_g07_th3_flag_N1c3!}
