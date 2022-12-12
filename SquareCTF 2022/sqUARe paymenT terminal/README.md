# sqUARe paymenT terminal

**150 points**

Found a capture of one of our hardware developers laptops...looks like it might contain a flag

*Given:* [Terminal_Cap.sal](https://github.com/LeonGurin/SquareCTF-2022/blob/main/sqUARe%20paymenT%20terminal/Terminal_Cap.sal)

___

After unzipping the file we get metadata jason and channels 0-7. 

Using google to figure out what `.sal` files are for I got to a [writeup](https://ctftime.org/writeup/27682) detailing the software and a near identical solution to our problem.

I installed `Logic 2` and used it to open the `.sal` file. we get some random data on channel 0.

Using the name of the question as a clue, I searched for the right bit-rate to put in the settings and found [this](https://www.sciencedirect.com/topics/computer-science/universal-asynchronous-receiver-transmitter#:~:text=UART%20interfaces%20have%20a%20maximum%20data%20rate%20of%20around%205%20Mbps.) detailing the different potential bit-rates for `UART`s which are as specified:

`There are many different speeds supported on UARTS: 300, 600, 1200, 1800, 2400, 4800, 7200, 9600, 14,400, 19,200, 38,400, 57,600, and 115,200 baud. The most common speed used by default on systems is 9600.`

Trying each and every-one of those eventually lead me to choose `38,400` and looking inside the console we get the right flag:

![pic1.png](https://github.com/LeonGurin/SquareCTF-2022/blob/main/sqUARe%20paymenT%20terminal/pic1.png)

>flag{h4rdw4r3h4ck3r}
