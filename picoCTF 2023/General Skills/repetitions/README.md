# repetitions

**100 points**

AUTHOR: THEONESTE BYAGUTANGAZA

Description
Can you make sense of this file?
Download the file [here](https://github.com/LeonGurin/picoCTF-2023/blob/main/General%20Skills/repetitions/enc_flag).

___

I was stuck on this until I read the title with the hint again.

The file itself looks like standard `base64` encoding but decrypting it gives seemingly random text.

With the hint `Multiple decoding is always good.` I repeatedly decoded the output of the text until the flag plaintext was visible:

> picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}
