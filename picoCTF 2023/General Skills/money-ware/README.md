# money-ware

**100 points**

AUTHOR: JUNI19

Description
Flag format: picoCTF{Malwarename}
The first letter of the malware name should be capitalized and the rest lowercase.
Your friend just got hacked and has been asked to pay some bitcoins to 1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX. He doesn’t seem to understand what is going on and asks you for advice. Can you identify what malware he’s being a victim of?

___

Googling `1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX` I got the [link](https://www.bitcoinabuse.com/reports/1Mz7153HMuxXTuR2R1t78mGSdzaAtNbBWX) which had reports with descriptions and one of those descriptions points us to:

More information here: [https://blog.avira.com/petya-strikes-back/](https://blog.avira.com/petya-strikes-back/)

This is an article about a vulnerability called `Petya` so our answer should be:

> picoCTF{petya}
