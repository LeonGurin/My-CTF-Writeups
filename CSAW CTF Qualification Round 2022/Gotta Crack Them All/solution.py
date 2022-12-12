
# enc = b'kz\xc6\xb9\xd9Du\xcb\x8a\x9e\xe0\x9d\xbeo\xee\x03\xcf\xddd'

# with open('leaked_password.txt','r') as f:
#     pas = f.read()
enc = b'`z\xce\xac\xc1Y6\xc1\x8a\x9d\xe0\x9d\xaas\xadj\xe8\xc6h\xfd\xf8\xd2\xa7\x9c'
pas = 'Hakamo-o-Dragon-Fighting'

i = 0
j = 0
key = b''
while j < len(enc):
    if (ord(pas[j]) ^ i).to_bytes(1,'big') == enc[j].to_bytes(1,'big'):
        key += i.to_bytes(1,'big')
        j += 1
        i = 0
    else:
        i += 1

print(f"the key is {key}")

with open('encrypted_passwords.txt', 'rb') as f:
    enc = f.read().splitlines()

def encrypt(plain):
	return b''.join((ord(x) ^ y).to_bytes(1,'big') for (x,y) in zip(plain,key))

dec = ''
for e in enc:
    i = 0
    j = 0
    k = 0
    while j < len(e):
        if k == len(key):
            k = 0
        if (i ^ key[k]).to_bytes(1,'big') == e[j].to_bytes(1,'big'):
            dec += chr(i)
            j += 1
            k += 1
            i = 0
        else:
            i += 1
    print(dec)
    dec = ''

