import subprocess

j = 2
enc = '111c0d0e150a0c151743053607502f1e10311544465c5f551e0e'

dec = 'buckeye{'
letter = 48

while 16+j < len(enc):
    
    proc = subprocess.Popen(['./sinep',dec+chr(letter)],stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        if line.rstrip()[9:] == enc.encode()[:16+j]:
            print(dec + chr(letter))
            # print(line.rstrip()[9:])
            j += 2
            dec = dec + chr(letter)
            letter = 47
            # print(enc.encode()[:16+j])
            # print(dec)
            break
    letter += 1

print(dec + '}')