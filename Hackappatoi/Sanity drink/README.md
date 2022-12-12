# Sanity drink

**50 points**

Find the password to enter a secret discobar where pwners beginners or expert can share their knowledge in the company of a beer

Author: @FRACCHETTO

nc hctf.hackappatoi.com 10001

*Given:* [sanity_drink](https://github.com/LeonGurin/Hackappatoi/blob/main/Sanity%20drink/sanity_drink)

___

Lets decompile with IDA and look inside:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char user_password[32]; // [rsp+0h] [rbp-50h] BYREF
  char otp_password[32]; // [rsp+20h] [rbp-30h] BYREF
  unsigned __int64 v7; // [rsp+48h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  puts("------------------------------------------------------------");
  puts("---------------[ Pwners Secret Club Access ]----------------");
  puts("------------------------------------------------------------");
  memset(user_password, 0, sizeof(user_password));
  memset(otp_password, 0, sizeof(otp_password));
  generate_otp(otp_password, 32);
  printf("Enter password: ");
  fgets(user_password, 50, _bss_start);
  user_password[strcspn(user_password, "\n")] = 0;
  if ( !user_password[0] )
  {
    puts("Invalid input...");
    exit(1);
  }
  if ( !strcmp(user_password, otp_password) )
  {
    puts("Authenticated!");
    system("/bin/sh");
  }
  else
  {
    puts("Authentication failed...");
  }
  return v7 - __readfsqword(0x28u);
}
```

Inspecting the code we can naturally guess that the vulnerability at play here is a classic `buffer overflow`.

BUT, the `fgets` lets us enter only 50 bytes into the buffer so how will we overwrite the 32 byte `otp` buffer with only 18 bytes left over?

This stumped me until I remembered how `strcmp` actually works.

It basically checks byte by byte until the terminating character `\0` is seen.

So we just have to insert the character ourselves.

when connecting to the application I inserted the string:

`a^Qaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa^Q`

The character `^@` is is `\0` and is entered with `CTRL + @`.

The string itself is 34 characters which overflows the user buffer and filles the otp buffer with `a\0`

When the strings are compared `strcmp` returns true because it only checks the first byte (until `\0`)

We get authenticated and we can cat the flag:

>HCTF{Ev3rY_p\/Vn_st4r7_w17h_dr1nk5}

