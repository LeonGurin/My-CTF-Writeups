# No way out

**200 points**

AUTHOR: KRIS

Description
Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform.
[Windows game](https://github.com/LeonGurin/picoCTF-2023/blob/main/Reverse%20Engineering/No%20way%20out/win.zip), Mac game

___

My very first introduction to unity hacking!

In the game you're spawned inside an area with a ladder but you can escape because of an invisible border.

After trying to look for the flag inside the files of the compiled game, I searched on google (and was probably put in a watchlist) on how to hack a unity game.

Ctf writeups pointed me to `dnSpy` a `C#` decompiling program that can be used to hack/mod unity games.

Using it and opening the games `Assembly-CSharp.dll` I could look inside the code.

In there I looked at the `PlayerController` class to see if I could make it so that I could jump infinitely to bypass the border.

I found this line of code that operates jumping:

```csharp
if (Input.GetButton("Jump") && this.canMove && this.characterController.isGrounded && !this.isClimbing)
{
    this.moveDirection.y = this.jumpSpeed;
}
```

and I removed the condition where it checks if the player is grounded from the `if` statement.

Compiling and exporting and opening the game once again, I could jump in the air to bypass the border and get outside the region where, when I went far enough gave the flag string in the middle of the string:

```
welcome_to_unity!!
```

So the flag was:

> picoCTF{welcome_to_unity!!}
