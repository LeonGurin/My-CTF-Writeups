# MSB

**200 points**

AUTHOR: LT 'SYREAL' JONES

Description
This image passes LSB statistical analysis, but we can't help but think there must be something to the visual artifacts present in this image...
Download the image [here](https://github.com/LeonGurin/picoCTF-2023/blob/main/Forensics/MSB/Ninja-and-Prince-Genji-Ukiyoe-Utagawa-Kunisada.flag.png)

___

This type of challenge can be easily solved with [StegSolve](https://stegonline.georgeom.net/) because this site can extract LSB data with pixel order and RGB values.

I tried the first default option -> the first row in this site and got readable words, so I downloaded the whole [file]() and `CTRL+F` the word `pico` I found the flag:

> picoCTF{15_y0ur_que57_qu1x071c_0r_h3r01c_06326238}
