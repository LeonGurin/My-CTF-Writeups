# Virtual Machine 0

**100 points**

AUTHOR: LT 'SYREAL' JONES

Description
Can you crack this black box?
We grabbed this design doc from enemy servers: [Download](https://github.com/LeonGurin/picoCTF-2023/blob/main/Reverse%20Engineering/Virtual%20Machine%200/Virtual-Machine-0.dae). We know that the rotation of the red axle is input and the rotation of the blue axle is output. The following input gives the flag as output: [Download](https://github.com/LeonGurin/picoCTF-2023/blob/main/Reverse%20Engineering/Virtual%20Machine%200/input.txt).

___

I searched google what the heck is a `.dae` file is, and its a file for models and can be opened in blender.

Opening the model in blender we get a lego construction with 2 wheels: 

* Blue - 8 teeth
* Red - 40 teeth

We're told that the input is the number of times we turned the red wheel and the output is the number of times we turned the blue wheel.

Turing the red wheel once rotates the blue wheel 5 times so that's their relationship (idea from the hint), so if we just multiply the input by 5 we get the output which is a number that's supposed to be the flag. 

There's only one thing to do now and it's to decode it to bytes:

```python
from Crypto.Util.number import long_to_bytes

n = 39722847074734820757600524178581224432297292490103995908738058203639164185
print(long_to_bytes(n*5))
```

And we get the flag:

> picoCTF{g34r5_0f_m0r3_3537e50a}
