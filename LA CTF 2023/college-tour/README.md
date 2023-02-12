# web/college-tour

**100 points**

Welcome to UCLA! To explore the #1 public college, we have prepared a scavenger hunt for you to walk all around the beautiful campus.

[college-tour.lac.tf](https://college-tour.lac.tf/)

___

We need to find 6 flags to merge into the final flag, let's find them!

The flags `1,2,4` can be found in the html of the page:

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <title>A tour of UCLA</title>
        <link rel="stylesheet" href="index.css">
        <script src="script.js"></script>
    </head>
    <body>
        <h1>A tour of UCLA</h1>
        <button id="dark_mode_button" onclick="dark_mode()">Click me for Light Mode!</button>
        <p>
            After finally setting foot on UCLA's campus, you're excited to explore it. However, the new student advisors have hidden <b>six</b>
            clues in the format lactf{number_text} all across UCLA. To complete the scavenger hunt, you must merge all the parts into one in order. For example, if you find the clues lactf{1_lOsT}, lactf{2__!N_b} (note the repeated underscore), and lactf{3_03LT3r}, the answer is lactf{lOsT_!N_b03LT3r}. Have fun exploring!
        </p>
        <!-- lactf{1_j03_4}-->
        <img src="royce.jpg" alt="lactf{2_nd_j0}" height="400px">
        <iframe src="lactf{4_n3_bR}.pdf" width="100%" height="500px"></iframe>
    </body>
```

1. The comment
2. The `alt` property of the `img` tag
4. The `src` property of the `iframe`

The third flag can be found in the `css` file in a `secret`:

```css
.secret {
    font-family: "lactf{3_S3phI}"
}
```

The final two, `5,6` can be found in the javascript:

```javascript
function dark_mode() {
    dark = 1 - dark;
    var element = document.body;
    element.classList.toggle("dark-mode");
    if (dark === 1) {
        document.getElementById("dark_mode_button").textContent = "Click me for Light Mode!";
    }
    else if (dark === 0) {
        document.getElementById("dark_mode_button").textContent = "Click me for Dark Mode!";
    }
    else {
        document.getElementById("dark_mode_button").textContent = "Click me for lactf{6_AY_hi} Mode!";
    }
}

window.addEventListener("load", (event) => {
    document.cookie = "cookie=lactf{5_U1n_s}";
});
``` 

The cookie is `document.cookie = "cookie=lactf{5_U1n_s}";`

And the last part is in the  `document.getElementById("dark_mode_button").textContent = "Click me for lactf{6_AY_hi} Mode!";`

The merged flag is:

> lactf{j03_4nd_j0S3phIn3_bRU1n_sAY_hi}

