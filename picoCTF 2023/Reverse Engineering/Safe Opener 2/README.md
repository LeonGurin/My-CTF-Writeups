# Safe Opener 2

**100 points**

AUTHOR: MUBARAK MIKAIL

Description
What can you do with this file?
I forgot the key to my safe but this [file](https://github.com/LeonGurin/picoCTF-2023/blob/main/Reverse%20Engineering/Safe%20Opener%202/SafeOpener.class) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?

___

Using an online java decompiler like [this one](http://www.javadecompilers.com/) we get the following code:

```java
import java.io.IOException;
import java.util.Base64;
import java.io.Reader;
import java.io.BufferedReader;
import java.io.InputStreamReader;

// 
// Decompiled by Procyon v0.5.36
// 

public class SafeOpener
{
    public static void main(final String[] args) throws IOException {
        final BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        final Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        for (int i = 0; i < 3; ++i) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();
            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
            final boolean isOpen = openSafe(encodedkey);
            if (isOpen) {
                break;
            }
            System.out.println("You have  " + (2 - i) + " attempt(s) left");
        }
    }
    
    public static boolean openSafe(final String password) {
        final String encodedkey = "picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}";
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        System.out.println("Password is incorrect\n");
        return false;
    }
}
```

and so the flag is:

> picoCTF{SAf3_0p3n3rr_y0u_solv3d_it_b427942b}
