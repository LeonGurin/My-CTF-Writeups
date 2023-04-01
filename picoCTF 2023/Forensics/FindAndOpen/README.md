# FindAndOpen

**200 points**

AUTHOR: MUBARAK MIKAIL

Description
Someone might have hidden the password in the trace file.
Find the key to unlock [this file](https://github.com/LeonGurin/picoCTF-2023/blob/main/Forensics/FindAndOpen/flag.zip). This [tracefile](https://github.com/LeonGurin/picoCTF-2023/blob/main/Forensics/FindAndOpen/dump.pcap) might be good to analyze.

___

This was a kinda random challenge, using `strings` on the `.pcap` file I got a lot of random stuff but in between it there were a could of messages of interest:

```
Flying on Ethernet secret: Is this the flag
iBwaWNvQ1RGe1Could the flag have been splitted?
AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=
PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
PBwaWUvQ1RGe1Maybe try checking the other file
```

Well basically I thought that the string:

`AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=`

was a base64 string but decoding it seperatly got nothing, and well if the file said: "Could the flag have been splitted?" I tried arranging:

```
iBwaWNvQ1RGe1, AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8= and PBwaWUvQ1RGesabababkjaASKBKSBACVVAVSDDSSSSDSKJBJS
```

One after another to get something.

When I decoded the string: `iBwaWNvQ1RGe1PBwaWUvQ1RGe1AABBHHPJGTFRLKVGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=` in cyberchef I got the output:

```
...(garbage)This is the secret: picoCTF{R34DING_LOKd_
```

Well using it as the password to unlock the zip revealed a file which had the flag:

> picoCTF{R34DING_LOKd_fil56_succ3ss_cbf2ebf6}
