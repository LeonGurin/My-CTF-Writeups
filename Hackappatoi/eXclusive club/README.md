# eXclusive club

**50 points**

I have opened a new exclusive club, but you will need a password to join!

Author: @R3tr0

*Given:* [eXclusiveclub](https://github.com/LeonGurin/Hackappatoi/blob/main/eXclusive%20club/eXclusiveclub)

___

If we use `IDA` and disassemble `main` we get the following pseudocode:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v3; // edx
  __int64 v5; // [rsp+18h] [rbp-28h]
  char s[24]; // [rsp+20h] [rbp-20h] BYREF
  unsigned __int64 v7; // [rsp+38h] [rbp-8h]

  v7 = __readfsqword(0x28u);
  printf("Welcome to our eXclusive club.\nType your password to join us.\n>");
  __isoc99_scanf("%s", s);
  v5 = obfuscation(s);
  v3 = strlen(s);
  if ( (unsigned int)check_access(v5, v3) )
    puts("Access granted, bro!");
  else
    puts("You can't join us this time...");
  return 0;
}
```

We can see 2 function now, `obfuscation` and `check_access`, lets look inside both of them and understand them:

**obfuscation:**

```c
_DWORD *__fastcall obfuscation(const char *a1)
{
  size_t v1; // rax
  int i; // [rsp+10h] [rbp-20h]
  _DWORD *v4; // [rsp+18h] [rbp-18h]

  v1 = strlen(a1);
  v4 = malloc(4 * v1);
  for ( i = 0; i < strlen(a1); ++i )
    v4[i] = a1[i] ^ 0x41;
  return v4;
}
```

This piece of code takes a string and `xors` it with `0x41`

**check_access:**

```c
__int64 __fastcall check_access(const char *a1, int a2)
{
  __int64 result; // rax
  int i; // [rsp+1Ch] [rbp-74h]
  int v4[26]; // [rsp+20h] [rbp-70h]
  unsigned __int64 v5; // [rsp+88h] [rbp-8h]

  v5 = __readfsqword(0x28u);
  result = 0LL;
  v4[0] = 41;
  v4[1] = 34;
  v4[2] = 53;
  v4[3] = 39;
  v4[4] = 58;
  v4[5] = 36;
  v4[6] = 25;
  v4[7] = 34;
  v4[8] = 45;
  v4[9] = 20;
  v4[10] = 116;
  v4[11] = 112;
  v4[12] = 55;
  v4[13] = 114;
  v4[14] = 30;
  v4[15] = 113;
  v4[16] = 51;
  v4[17] = 31;
  v4[18] = 15;
  v4[19] = 113;
  v4[20] = 53;
  v4[21] = 126;
  v4[22] = 60;
  if ( a2 != 23 )
    return 0LL;
  for ( i = 0; i <= 22; ++i )
  {
    result = (unsigned int)v4[i];
    if ( *(_DWORD *)&a1[4 * i] != (_DWORD)result )
      return 0LL;
    if ( i == 22 )
      return 1LL;
  }
  return result;
}
```

This function checks the previous string with the values in `v4`. (note, the `4*i` confused me before I changed the `a1` variable type from int to char* in the in IDA because I did not realize that the purpose of the multiplication is to return one byte of memory)

We would like to find out what the obfuscated string was before the function and so I wrote the following code:

```c
#include <stdio.h>

int main(){
    int v4[26]; 

    int result = 0LL;
    v4[0] = 41;
    v4[1] = 34;
    v4[2] = 53;
    v4[3] = 39;
    v4[4] = 58;
    v4[5] = 36;
    v4[6] = 25;
    v4[7] = 34;
    v4[8] = 45;
    v4[9] = 20;
    v4[10] = 116;
    v4[11] = 112;
    v4[12] = 55;
    v4[13] = 114;
    v4[14] = 30;
    v4[15] = 113;
    v4[16] = 51;
    v4[17] = 31;
    v4[18] = 15;
    v4[19] = 113;
    v4[20] = 53;
    v4[21] = 126;
    v4[22] = 60;
    for (int i = 0; i <= 22; ++i )
    {
        printf("%c", v4[i]^0x41);
    }
}
```

This code takes the parameters stored in v4 and xors them with `0x41` because thats the value of the original string.

If we compile and run this code we get the flag!

>hctf{eXclU51v3_0r^N0t?}