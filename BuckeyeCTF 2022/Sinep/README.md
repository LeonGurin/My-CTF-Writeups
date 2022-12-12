# Sinep

**50 points**

Sinep industries is advertising a Certified unbreakable encryption algorithm. Seeing as it's proprietary and Certified, I'm confident my data is safe. I'm so confident I'll straight up give you the flag.... ENCRYPTED hahahaha 0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e

*Given:* [sinep](https://github.com/LeonGurin/BuckeyeCTF-2022/blob/main/Sinep/sinep)

___

After playing around, I noticed that by entering each letter it gives a deterministic response which we could exploit with for loops.

the template `buckeye{` matched perfectly so I decided to loop through the next letters and numbers to see if the output of the program was consistent with out given encryption: `0x111c0d0e150a0c151743053607502f1e10311544465c5f551e0e`

And so I coded the following program that takes the string `buckeye{ + letters/numbers` as a parameter and I checked the programs output against the key to continue:

```python
import subprocess

j = 2
enc = '111c0d0e150a0c151743053607502f1e10311544465c5f551e0e'

dec = 'buckeye{'
letter = 48

while 16+j < len(enc):
    
    proc = subprocess.Popen(['./sinep',dec+chr(letter)],stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        if line.rstrip()[9:] == enc.encode()[:16+j]:
            print(dec + chr(letter))
            j += 2
            dec = dec + chr(letter)
            letter = 47
            break
    letter += 1

print(dec + '}')
```

and so the final line of the program reads:

>buckeye{r3v_i5_my_p45510n}
