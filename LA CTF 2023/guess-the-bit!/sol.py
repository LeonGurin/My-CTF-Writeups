from pwn import *
import gmpy2

io = remote('lac.tf', 31190)

io.recvuntil('n =  ')
n = int(io.recvline().strip())

io.recvuntil('a =  ')
a = int(io.recvline().strip())

for i in range(150):
    io.recvuntil('c =  ')
    c = int(io.recvline().strip())
    if gmpy2.is_square(c):
        print(f'SENT: {0}')
        io.sendline(b'0')
    else:
        print(f'SENT: {1}')
        io.sendline(b'1')
    
print(io.recvline().strip())
print(io.recvline().strip())
io.close()



