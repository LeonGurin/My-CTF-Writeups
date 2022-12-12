# Grab a beer and disappear

**50 points**

Today i’ve noticed that the free access internet computer of my pub does not work anymore. I remember a groups of 5 people that this weekend was playing with it. I’ve managed to recover the disks images from it. Can you help me fix it and recover the files?

@isfet

*Given:* chall.zip

___

Well this was a weird one, I unzipped and got 3 files: `disk0,disk1,disk2`

using `file *` and got:

```
disk0: DOS/MBR boot sector; partition 1 : ID=0xfd, start-CHS (0x0,32,33), end-CHS (0xc,190,50), startsector 2048, 202752 sectors, extended partition table (last)
disk1: data
disk2: DOS/MBR boot sector; partition 1 : ID=0xfd, start-CHS (0x0,32,33), end-CHS (0xc,190,50), startsector 2048, 202752 sectors, extended partition table (last)
```

disk1 seems to have only data so I wanted to `cat` its contents and the very last line was:

`   uxQ4ZcaL8a05ąCbb20;9cm]%y.n3ver_G1v3_4_Pc_t0_druNk_p30pL3!!`

which was actually the flag... 👀
welp:

>HCTF{n3ver_G1v3_4_Pc_t0_druNk_p30pL3!!}

