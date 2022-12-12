# Gotta Crack Them All

**xxx points**

Isn't the Word Wide Web a fascinating place to be in? Words.. so many words.. all linked... NOTE: The flag doesn't have a wrapper. It needs to be wrapped with curly brackets and please put CTF in front of the curly brackets.

[http://web.chal.csaw.io:5010](http://web.chal.csaw.io:5010)

___

Loading the webpage we get to a page with loads of words that only 1-3 of them are linked to another webpage.

Each time we go to the next webpage, there is another link. Maybe if we could automate the process, there would be an end 👀

And so with a suggestion from my teammate I tried to use `python requests` to automate it.

I wrote the following code:

```python
import requests

word = 'stuff'
while True:
    flag = True
    r = requests.get("http://web.chal.csaw.io:5010/" + word)
    print(r.text)
    lines = r.text.splitlines()
    for line in lines:
        if flag == True:
            if  "_" in line or "href" in line and (line.lstrip()).startswith("<a"):
                print(line)
                if "_" in line:
                    exit()
                else:
                    word = line.split('"')[1][1:]
                    if word == "Booooo!":
                        print("Done!")
                        exit()
                print(word)
                flag = False
        else:
            break
```

This code worked only on the first request but locked up afterwards.

My teammate looked at my code and added cookies to the requests sent and it worked perfectly.
His newly working code is:

```python
import requests

word = 'stuff'
tmp_s = "stuff"
while True:
    flag = True
    c = {"solChain": tmp_s}
    r = requests.get("http://web.chal.csaw.io:5010/" + word, cookies= c)
    print(r.content)
    lines = r.text.splitlines()
    #print(lines)
    for line in lines:
        if flag == True:
            if  "_" in line or "href" in line and (line.lstrip()).startswith("<a"):
                #print(line)
                if "_" in line:
                    exit()
                else:
                    word = line.split('"')[1][1:]
                    tmp_s += " " + word
                    if word == "Booooo!":
                        print("Done!")
                        exit()
                print(word)
                flag = False
        else:
            break
```

the final line is:

> CTF{w0rdS_4R3_4mAz1nG_r1ght}
