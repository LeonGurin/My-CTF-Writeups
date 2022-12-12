# Heaven

**426 points**

"I was in the seventh heaven painted red green and blue"

_Given:_ [Seventh_Heaven_Image](https://github.com/LeonGurin/Shell-CTF-2022/blob/main/Heaven/Seventh_Heaven_Image.jpeg)

___

The clue guides us to search the `RGB` plains of the image.

The only way I know how is using `StegOnline` tool. Clicking `Extract Files/Data` we are greeted with the option to extract RGB values, checking the 7th pixel for each color and extracting gives us the following string:

`SHELL{ma  n1pul4t1  ng_w1th_  31ts_15_  3A5y}`

Formatting it just right gives us the flag:

>SHELL{man1pul4t1ng_w1th_31ts_15_3A5y}