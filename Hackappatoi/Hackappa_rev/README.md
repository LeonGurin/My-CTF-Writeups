# Hackappa_rev

**50 points**

Here we are again, this is our favorite pub! You can take the flag and come back without getting drunk in the process?

Author: @Unleashed

*Given:* [hackappa_rev](https://github.com/LeonGurin/Hackappatoi/blob/main/Hackappa_rev/hackappa_rev)

___

If we use `IDA` and disassemble `main` we get the following pseudocode:

```c
int __cdecl __noreturn main(int argc, const char **argv, const char **envp)
{
  int v3[2]; // [rsp+8h] [rbp-8h] BYREF

  puts("Welcome to the Hackappapub ! ");
  while ( 1 )
  {
    puts("What do you want to drink ?");
    puts("1)Hackappa beer");
    puts("2)Hackappa Cocktail");
    puts("3)Hackappacola ");
    v3[0] = 0;
    __isoc99_scanf("%d", v3);
    holder((unsigned int)v3[0]);
    if ( b == 6 && c == 6 && h == 6 )
      break;
    if ( b == 10 && c == 7 && h == 11 )
      decrypt();
  }
  v3[1] = out();
  exit(1);
}
```

We can see another function named `decrypt` let's look inside its disassembly:

```c
__int64 decrypt()
{
  __int64 v1[3]; // [rsp+0h] [rbp-20h] BYREF
  int i; // [rsp+1Ch] [rbp-4h]

  qmemcpy(v1, "KFWI~6}bGuxqnbU6y", 17);
  printf("%s", (const char *)v1);
  for ( i = 0; i <= 99 && *((_BYTE *)v1 + i); ++i )
    *((_BYTE *)v1 + i) -= 3;
  printf("%s}\n", (const char *)v1);
  return 0LL;
}
```

As we can see it does some byte operations on the string `KFWI~6}bGuxqnbU6y`, lets try to rewrite this code to look more normal in `c` and run it:

```c
#include <stdio.h>

int main(){
    char v1[17] = "KFWI~6}bGuxqnbU6y";
    printf("%s\n", (const char *)v1);
    for (int i = 0; i <= 99 && *(v1 + i); ++i ){
        *(v1 + i) -= 3;
    }
    printf("%s}\n", (const char *)v1);
}
```

If we compile and run this code we get the flag!

>HCTF{3z_Drunk_R3vlF|}