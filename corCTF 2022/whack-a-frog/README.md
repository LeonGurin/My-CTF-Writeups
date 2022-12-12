**forensics/whack-a-frog** 

*jammy + chop0*

Come play a game of Whack-a-Frog [here](https://whack-a-frog.be.ax/) and let all your anger out on the silly msfrogs. Due to lawsuits by Murdoch, we were forced to add DRM protection, which has allowed us to detect a player distributing copyrighted media. Thankfully, we took a pcap: can you make out what he was sharing? Make sure that anything you find is all typed in UPPERCASE and is wrapped like corctf{text}. Best of luck and enjoy whacking some frogs!

_Downloads_ [whacking-the-froggers.pcap](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/whacking-the-froggers.pcap)

___

Going into the website link we are greeted with a grid which we can "draw".

Opening the `pcap` file in `Wireshark` and following the `TCP` steam we can see many `GET` requests with to some domain with 3 parameters passed: x, y and event.

My first attempt was to extract the x and y values using the `filter` option in `Cyberchef` like so:

![img1](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img1.png)

Saving the output to a file (promptly named a.txt like a proffesional) and running:

>cat a.txt | grep -o "x=\[0-9]\*&y=\[0-9]*" > d.txt

got me a new file which I used cyberchef again to turn to real coordinates using the `find/replace` operation.

in the end I got a large file with correctly formatted coordinates.

Plugging them straight into `Desmos` got me this picture:

![img2](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img2.png)

this resembles text but is mostly gibberish. 

I noticed that there where 3 types of events send in the `GET` request which were:

* mousemove
* mouseup
* mousedown

I tried extracting only `mouseup/down/move` points and plotting them to no avail.

I asked my teamates for help and after many hours they told me about the `Turtle` python module which draws acording to point coordinates, this way we will be able to know how the person wrote his message.

Knowing this, I did everything like before with the addition of specifying the event type with grep:

>cat a.txt | grep -o "x=\[0-9]\*&y=\[0-9]*&event=mouse\[m|u|d]" > d.txt

which allows me to add the `penup()` and `pendown()` commands to the script.

The exact way I constructed the Turtle instructions with `Cyberchef` are shown here:

![img3](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img3.png)

![img4](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img4.png)

The final python script looks like this (the full version is [here](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/tur.py))

```python
import turtle

t = turtle.Turtle()

t.color('red')
t.width(5)

t.setpos(-200+365,10)
t.setpos(-200+295,20)
t.setpos(-200+204,31)
t.setpos(-200+105,39)
t.setpos(-200+82,39)
t.setpos(-200+65,37)
t.setpos(-200+54,34)
t.setpos(-200+50,34)
t.setpos(-200+39,30)
t.setpos(-200+37,29)
t.setpos(-200+34,26)
t.setpos(-200+33,25)
t.setpos(-200+31,22)
t.setpos(-200+30,21)
t.setpos(-200+26,20)

# more in the real script 
```

(Note: I added `-200+` because Turtle draws from the center of the screen and the picture goes outside the frame without it)

With this script we get an animation of the drawing.

Partway the one who drew this goes again to intensify the letter thus making it more obscure so when I looked at the picture before that:

![img5](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img5.png)

I realised that the `Gamma looking letter` is the letter `L` rotated and flipped.

Doing exactly that gives us:

![img6](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img6.png)

or better:

![img7](https://github.com/LeonGurin/corCTF-2022/blob/main/whack-a-frog/img7.png)

Stating the truth, we could have figured the rotation and flipping with the Desmos image but for the longest time we thought that the letters where the right way around and we could not figure out the right letter, our best guesses for the flag were:

 * corctf{DIRAXOX}
 * corctf{DIRHXDX}
 * corctf{DINAXQX}

and many many more permutations than that.

The final flag turned out to be the following:

>corctf{LILYXOX}