# crypto/rolling in the mud

**179 points**

uugh, these pigs in my pen are making a complete mess! They're rolling all over the place!

Anyway, can you decode this cipher they gave me, almost throwing it at me while rolling around?

Answer in lowercase with symbols. In the image, { and } are characters that should appear in your flag, and replace spaces with _.

*Given:* [cipher.png](https://github.com/LeonGurin/LA-CTF-2023/blob/main/rolling%20in%20the%20mud/cipher.png)

___

The easiest part is guessing which cipher is used.

With strange picture ciphers the clues are within the text to guess its name and the most prominent thing were the `pigs` in the text which were rolling in a `pen` and so the right cipher is a `pigpen` cipher.

Cool so we can use `decodeFr` and decrypt it right? It would seem so but copying the symbols in the picture did not result in the right decryption until you realize that the picture is `UPSIDE DOWN!`, the flag string `lactf` was at the end and the dot at the front was the full-stop of the sentence.

Copying the upside down symbols gives us the right cipher which is:

> lactf{rolling_anm_rolling_anm_rolling_vntil_the_pigs_go_home}
