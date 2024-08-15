# web/traversed

**240 solves / 123 points**
*Auther: halp*

I made this website! you can't see anything else though... right?? URL: http://litctf.org:31778/
___

Looking inside the `URL` we get the text: 

"Welcome! The flag is hidden somewhere... Try seeing what you can do in the url bar. There isn't much on this page..."

After messing with most things we could exploit in the website, the challenge name reminded me of a vulnerability I found in the **INCD 2022** competition which exploited a path traversal vulnerability of an `Apache 2.4.49` server.

The vulnerability exploits the directory `/cgi-bin/` and with it we can append url-encoded `..` characters to go through the filesystem of the server.

So, sending a GET request to:

`http://litctf.org:31778/cgi-bin/.%2e/.%2e/.%2e/.%2e/etc/passwd`

we actually get the file!

But... no flag.

Me and my teammate looked everywhere, we looked inside the *unusual* user `node`'s directory and `.bashrc` files and other common paths like: `/etc/shadow`, `/var/www/html` while searching for known files in linux.

After a lot of time we figured maybe it's stored in the classic ctf-style `flag.txt` but still couldn't find it.

I opened a ticket to the organizers and they confirmed to me that i looked in the right direction and with a sleep break, the next day I randomly sent requests and finally the request to:

`http://litctf.org:31778/cgi-bin/.%2e/.%2e/flag.txt`

worked.

Welp,

> LITCTF{backtr@ked_230fim0}
