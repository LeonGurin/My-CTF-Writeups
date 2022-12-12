# Best videogame

**328 points**

Can you guess what is my favourite videogame saga? I hope you like it too!

Author: @R3tr0

*Given:* [bestvideogame](https://github.com/LeonGurin/Hackappatoi/blob/main/Best%20videogame/bestvideogame)

___

If we use `IDA` and disassemble `main` we get the following pseudocode:

```c
int __cdecl main(int argc, const char **argv, const char **envp)
{
  void *v4; // rsp
  const char **v5; // [rsp+8h] [rbp-F0h] BYREF
  int v6; // [rsp+14h] [rbp-E4h]
  int k; // [rsp+24h] [rbp-D4h]
  int j; // [rsp+28h] [rbp-D0h]
  int i; // [rsp+2Ch] [rbp-CCh]
  int v10; // [rsp+30h] [rbp-C8h]
  unsigned int v11; // [rsp+34h] [rbp-C4h]
  __int64 v12; // [rsp+38h] [rbp-C0h]
  __int64 v13; // [rsp+40h] [rbp-B8h]
  const char ***v14; // [rsp+48h] [rbp-B0h]
  __int64 v15; // [rsp+50h] [rbp-A8h]
  int v16[26]; // [rsp+58h] [rbp-A0h]
  unsigned __int64 v17; // [rsp+C0h] [rbp-38h]

  v6 = argc;
  v5 = argv;
  v17 = __readfsqword(0x28u);
  if ( argc == 3 )
  {
    v16[0] = 61;
    v16[1] = 164;
    v16[2] = 170;
    v16[3] = 39;
    v16[4] = 239;
    v16[5] = 123;
    v16[6] = 13;
    v16[7] = 77;
    v16[8] = 104;
    v16[9] = 196;
    v16[10] = 194;
    v16[11] = 153;
    v16[12] = 26;
    v16[13] = 117;
    v16[14] = 248;
    v16[15] = 2;
    v16[16] = 50;
    v16[17] = 15;
    v16[18] = 139;
    v16[19] = 116;
    v16[20] = 25;
    v16[21] = 151;
    v16[22] = 157;
    v10 = strlen(v5[2]);
    v11 = strlen(v5[1]);
    if ( !strcmp(v5[1], "play") )
    {
      if ( v10 == 23 )
      {
        v12 = generatekey(v5[1]);
        v13 = 22LL;
        v4 = alloca(96LL);
        v14 = &v5;
        for ( i = 0; i < v10; ++i )
          *((_DWORD *)v14 + i) = v5[2][i];
        v15 = RC4(v12, v14, v11, (unsigned int)v10);
        for ( j = 0; ; ++j )
        {
          if ( j >= v10 )
            return 0;
          if ( *(_DWORD *)(4LL * j + v15) != v16[j] )
          {
            puts("You got the console right, but not the game :(\nTry again!");
            return 0;
          }
          if ( j == v10 - 1 )
            break;
        }
        printf("Correct! Here is your prize!\nhctf{");
        for ( k = 0; k < v10; ++k )
          putchar(*((_DWORD *)v14 + k));
        puts("}");
        return 0;
      }
      else
      {
        puts("You got the console right, but not the game :(\nTry again!");
        return 0;
      }
    }
    else
    {
      puts("Mmh the console is not correct :/\nTry again!");
      return 0;
    }
  }
  else
  {
    puts("Discover my favourite videogame saga!\nUsage:\n\t./bestvideogame <console> <myfavouritesaga>");
    return 0;
  }
}
```

This code is long and confusing but we can start to understand it bit by bit.

The first part is realizing that the first argument for the program is in `v5[1]` and is compared to the string "play".

That was easy but the second argument is much more difficult to understand.

We can notice that the condition to enter the correct printf is successfully comparing to each letter in `v16` with the variable `v15`.

the `v5` variable is given to us from the function `RC4`. `RC4` is a type of stream cipher which we know the source code for and encrypt and decrypt data from.

Lets use it to our advantage and find the decryption of the 23 bytes given in `v16` to get `v15`.

in order to encrypt a string we need a key. 

Thankfully, we have `v12` to thank for that which gets generated with `generatekey`

The code for this function is basically copying the bytes from the argument given and saving it:

```c
_DWORD *__fastcall generatekey(const char *a1)
{
  int i; // [rsp+10h] [rbp-10h]
  int v3; // [rsp+14h] [rbp-Ch]
  _DWORD *v4; // [rsp+18h] [rbp-8h]

  v3 = strlen(a1);
  v4 = malloc(4LL * v3);
  for ( i = 0; i < v3; ++i )
    v4[i] = a1[i];
  return v4;
}
```

and so we now have the key:

```
v12 = generatekey(v5[1]); --> "play"
v12 = "play"
```

and if we plug each value of `v16` as the ciphertext and `play` as the key in `decode.fr`

we get the string - `R351d3N7_3viL_5CarY_Uh?`

and so the flag is:

>hctf{R351d3N7_3viL_5CarY_Uh?}