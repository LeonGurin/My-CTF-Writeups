# crypto/greek cipher

**254 points**

You think you've seen all of the "classic" ciphers? Instead of your standard cipher, I've created my own cipher: the monoalphagreek cipher!

Answer with just the flag in lowercase with symbols left in.

*Given:* [greek.txt](https://github.com/LeonGurin/LA-CTF-2023/tree/main/greek%20cipher/greek.txt)

___

The way I solved this was sort of intuitive.

I used `CyberChef` to find and replace letters I can infer with the information I have.

Right away `lactf` can be decoded from the flag format.

The letter `i` can be seen alone so that was a giveaway.

Because the first sentence is a question I guessed that the first word is `did` and it matches the `i` we found.

The 2 questions in the plaintext started with `did ωπν αζπλ tηat` and I guessed that it said `did you know` and so on, the more you uncover the easier it gets.

the flag turns out to be:

> lactf{i_guess_using_many_greek_characters_didn't_stop_you._well_played_i_must_say.congrats!}
