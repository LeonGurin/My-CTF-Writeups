
enc = '8~p*m~`>'

def tryXor(msg,letter,key2):
    key = 0
    while chr(ord(msg) ^ key) != letter:
        key = key+1
    print(f'key for {letter} is {chr(key)}')
    key2 = key2.join(chr(key))
    return key2

def xor(msg):
    i = 0
    key2 = ''

    key2 += tryXor(msg[i],'S',key2)
    i += 1
    key2 += tryXor(msg[i],'H',key2)
    i += 1
    key2 += tryXor(msg[i],'E',key2)
    i += 1
    key2 += tryXor(msg[i],'L',key2)
    i += 1
    key2 += tryXor(msg[i],'L',key2)
    i += 1
    key2 += tryXor(msg[i],'{',key2)

    print(f'key up till now: {key2}')
print(xor(enc))

# SHELL{X0R_1S_R3VeR51BL3}
