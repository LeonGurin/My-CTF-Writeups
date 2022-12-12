with open('megaxord.txt', 'r') as f:
    enc = f.read()

with open('megaxord_dec.txt', 'w') as g:
    i=0
    while i<256:
        for letter in enc:
            try:
                g.write(chr(ord(letter) ^ i))
            except:
                g.write('\n\n')
        i += 1