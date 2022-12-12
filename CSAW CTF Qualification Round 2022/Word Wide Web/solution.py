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

