# BrainDrunk

**460 points**

Oh S**t, I'm so in hangover I cannot even remember what I was doing, my code will never pass the review

Author: @diegosona

*Given:* [attachment](https://github.com/LeonGurin/Hackappatoi/blob/main/BrainDrunk/attachment.txt)

___

When I saw the question I thought about `Brainfuck` straight away, and so I made a python script to convert the emojis to the relevant `brainfuck` characters.

As I have not tried writing in `brainfuck` I did not have the slightest clue as to what character should be mapped where and so I read the wiki and realized that `brainfuck` has actually 8 symbols but we do not need `,` as I doubted that the program required inputs.

With trial and error and some realizations like that the characters `[` and `]` should not be the other way around and more I finally got the right conversion like so:

```py
with open('attachment.txt', 'r', encoding='utf8') as f:
    data = f.read()

for i in data:
    if i == '🥂':
        print('>', end='')
    elif i == '🍾':
        print('.', end='')
    elif i == '🍷':
        print('-', end='')
    elif i == '🍸':
        print('[', end='')
    elif i == '🍹':
        print('<', end='')
    elif i == '🍺':
        print('+', end='')
    elif i == '🥃':
        print(']', end='')
```

The output for this program I plugged into decode.fr's interpreter.

The output was: `Do you want a drink ?`

Somewhat strangely the memory for the program has the start of the flag with: `HCTF{D0nt_`.

After some time I thought about looking at the memory in real time to see if the flag and I found this interpreter: [link](https://brainfuck.michd.me/).

Using this site I could pass step by step and the whole flag was written there before the `Do you want a drink ?` string was loaded and so the flag is:

>HCTF{D0nt_c0d3_1f_y0u_4R3_s0b3R}

