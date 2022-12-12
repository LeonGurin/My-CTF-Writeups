# Gotta Crack Them All

**xxx points**

As an intern in the security department, you want to show the admin what a major security issue there is by having all passwords being from a wordlist (even if it is one the admin created) as well as potential issues with stream ciphers. Here's the list of encrypted passwords (including the admin's), the encryption algorithm and your password. Can you crack them all and get the admin's password? Here is the web service that the admin made to encrypt a password: nc crypto.chal.csaw.io 5002

NOTE: The flag is just the admin's password.

*Given:* [encrypt.py](https://github.com/LeonGurin/CSAW-CTF-Qualification-Round-2022/blob/main/Gotta%20Crack%20Them%20All/encrypt.py) [leaked_password.txt](https://github.com/LeonGurin/CSAW-CTF-Qualification-Round-2022/blob/main/Gotta%20Crack%20Them%20All/leaked_password.txt) [encrypted_passwords.txt](https://github.com/LeonGurin/CSAW-CTF-Qualification-Round-2022/blob/main/Gotta%20Crack%20Them%20All/encrypted_passwords.txt)

___

Looking into the python script we can understand that the way they encrypted the passwords is a normal letter by letter xor cipher with a key.

So using the `netcat` provided I checked the encrypted version of the leaked password:

```
>> Cacturne-Grass-Dark
The encrypted password is: b'kz\xc6\xb9\xd9Du\xcb\x8a\x9e\xe0\x9d\xbeo\xee\x03\xcf\xddd'
```

and so I made a code to xor each letter with of `Cacturne-Grass-Dark` to get the encrypted letter.

```python
enc = b'kz\xc6\xb9\xd9Du\xcb\x8a\x9e\xe0\x9d\xbeo\xee\x03\xcf\xddd'

with open('leaked_password.txt','r') as f:
    pas = f.read()

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
```

and the output was the key: 

`the key is b'(\x1b\xa5\xcd\xac6\x1b\xae\xa7\xd9\x92\xfc\xcd\x1c\xc3G\xae\xaf\x0f'`

I then added a script to decrypt each password with this key:

```python
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
```

and I got the following output:

```
Kingler-Water      
Darkrai-Dark       
Chingling-Psychic  
Happiny-Normal     
Clawitzer-Water    
Cacturne-Grass-Dark
Slowking-Poison-PsyÞÿwg
Sneasel-Dark-Ice
Hoopa-Psychic-Ghost
Rhyperior-Ground-RoÞü
Seedot-Grass
Chinchou-Water-ElecÉåwg
Tsareena-Grass
Excadrill-Ground-StØòr
Gumshoos-Normal
Kricketune-Bug
Dartrix-Grass-FlyinÚ
Pikipek-Normal-FlyiÓð
Dugtrio-Ground-SteeÑ
Basculin-Water
Hippowdon-Ground
Togetic-Fairy-FlyinÚ
Finneon-Water
Riolu-Fighting
Entei-Fire
Spritzee-Fairy
Mantine-Water-FlyinÚ
Silvally-Normal
Bellsprout-Grass-PoÔäqj
Wyrdeer-Normal-PsycÕþ}
Marill-Water-Fairy
Herdier-Normal
Altaria-Dragon-FlyiÓð
Thwackey-Grass
Spewpa-Bug
Bronzong-Steel-PsycÕþ}
Hakamo-o-Dragon-FigÕãwj0
Chespin-Grass
Mr. Mime-Psychic-FaÔåg
Tornadus-Flying
Pupitar-Rock-Ground
Combusken-Fire-FighÉþpc
Guzzlord-Dark-DragoÓ
Carnivine-Grass
Growlithe-Fire
Grubbin-Bug
Gastrodon-Water-GroÈùz
Goomy-Dragon
Thievul-Dark
1n53cu2357234mc1ph3
Seadra-Water
```

as you can see, some of the passwords that were longer than the leaked password had weird characters that were not right.

I noticed while looking at the passwords the password: `Mr. Mime-Psychic-FaÔåg` and realized that the passwords were pokemon and their types!

I grabbed the longest password I could find `Hakamo-o-Dragon-FigÕãwj0` and checked online what "Hakamo-o"s types are. And, not surprisingly, the password is supposed to be:

`Hakamo-o-Dragon-Fighting`

And so I entered it in the netcat script and got the encryption, found the key with the same code I wrote in the beginning and decrypted all of the passwords again.

```python
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
```

and my output was:

```
the key is b'(\x1b\xa5\xcd\xac6\x1b\xae\xa7\xd9\x92\xfc\xcd\x1c\xc3G\xae\xaf\x0f\x95\x8c\xbb\xc9\xfb'
Kingler-Water
Darkrai-Dark
Chingling-Psychic
Happiny-Normal
Clawitzer-Water
Cacturne-Grass-Dark
Slowking-Poison-Psychic
Sneasel-Dark-Ice
Hoopa-Psychic-Ghost
Rhyperior-Ground-Rock
Seedot-Grass
Chinchou-Water-Electric
Tsareena-Grass
Excadrill-Ground-Steel
Gumshoos-Normal
Kricketune-Bug
Dartrix-Grass-Flying
Pikipek-Normal-Flying
Dugtrio-Ground-Steel
Basculin-Water
Hippowdon-Ground
Togetic-Fairy-Flying
Finneon-Water
Riolu-Fighting
Entei-Fire
Spritzee-Fairy
Mantine-Water-Flying
Silvally-Normal
Bellsprout-Grass-Poison
Wyrdeer-Normal-Psychic
Marill-Water-Fairy
Herdier-Normal
Altaria-Dragon-Flying
Thwackey-Grass
Spewpa-Bug
Bronzong-Steel-Psychic
Hakamo-o-Dragon-Fighting
Chespin-Grass
Mr. Mime-Psychic-Fairy
Tornadus-Flying
Pupitar-Rock-Ground
Combusken-Fire-Fighting
Guzzlord-Dark-Dragon
Carnivine-Grass
Growlithe-Fire
Grubbin-Bug
Gastrodon-Water-Ground
Goomy-Dragon
Thievul-Dark
1n53cu2357234mc1ph32
Seadra-Water
```

and then we notice the only non pokemon and type password which is the admins password and the key:

>1n53cu2357234mc1ph32

I liked this challenge 😀