from itertools import cycle
pt = b"Long ago, the four nations lived together in harmony ..."

# key = cycle(b"lactf{??????????????}")

ct = "200e0d13461a055b4e592b0054543902462d1000042b045f1c407f18581b56194c150c13030f0a5110593606111c3e1f5e305e174571431e"

# convert ct to bytes
ct = bytes.fromhex(ct)
ret = ""

for i in range(len(pt)):
    b = (pt[i] ^ ct[i])
    ret += hex(b)[2:]

print(bytes.fromhex(ret))
