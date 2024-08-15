# misc/pokemon

**271 solves / 120 points**
*Auther: Stephanie*

I love pokemon! Win to get the flag

*Given: [pokemon.zip](https://github.com/LeonGurin/My-CTF-Writeups/tree/main/LITCTF%202024/pokemon/pokemon.zip)*

___

We're given a zip file that has a simple `html/css/js` webpage.

Running it locally we get a pokemon game that we can easily win by just pressing the attacking buttons.

When we win an "animation" of a person holding a flag runs and then it finishes.

Looking at the source-code we see that it runs the animation sequence by calling `win-sequence` that is defined inside the `.html` file.

```js
function showWinSequence() {
    const winSequenceElem = document.getElementById('win-sequence');
    const images = winSequenceElem.getElementsByClassName('win-image');
    //...
}
```

This sequence is just the 15 `.png` images in order.

The images themselves are a cipher called the `Flag Semaphore` and inputting the sequence inside [dcode.fr/semaphore-flag](https://www.dcode.fr/semaphore-flag) we get the flag.


