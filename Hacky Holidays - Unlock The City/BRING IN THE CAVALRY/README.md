**[25 POINTS]** *WHERE IT ALL STARTED* 

Look in the eyes chicho, they never lie
___
Unzipping the given file gives us 2 files: `key.txt` and `Trusted_Relationships.pdf`.

Using `file` on `key.txt` we can confirm that it is a pdf file. Converting to pdf gives us a picture with the words:
>N0_Brutef0rce

Looking into the pdf file, we are greeted with a password. Plugging `N0_Brutef0rce` gives us access to the PDF.

I've got to say, I did not know how to progess from here for the longest time until I decided to open it using adobe acrobat.

By accident I descoverd the `Attachments` button and there we get 2 new files, `flag1.txt` and `Silent_Attack.wav`.

The flag is inside the text file and is:
> CTF{Th1rd_P@rty_Vend0r5_@re_R15ky}

___
___

**[25 POINTS]** *TRYING TO BE RESILIENT*

It would be nice if we could see sounds.
___

Using the hint I opened the audio file in `Audacity` and looked at the spectrogram.

I looks just like a `QR Code!` maybe it is...

![img0](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/BRING%20IN%20THE%20CAVALRY/images/img0.png)

and so the long and tedious process of tracing it because a phone can't read it 😡

I got this:
![img1](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/BRING%20IN%20THE%20CAVALRY/images/img1.png)

which brings to this link: 
> https://mega.nz/file/GuQQjQjD#ofN2njJUk5zCxVI753BYUiBjUy30kArvLx8L9XJUZPY

Unzipping this file reveals again, 2 files: `flag2.txt` and `traffic.pcapng`
the flag is in the text file and is:
> CTF{Y0u_Better_5ecure_Y0ur_RDP}

___
___

**[50 POINTS]** *HIGH PRICE TAG*

How could they do this? This is devastating for our company!
___

Openning the `traffic.pcapng` file in wireshark and following the TCP stream I clicked on the first link in the HTTP request `https://mega.nz/file/zjYjTSAS#c2d5J5DIT_-idyvQ2JeAI2wHfITF7xJEAlViciizk8o`.

I brings to a download of another zip file called `Source_Code.zip`. Unzipping it, unsurprisingly gets us another 2 files.

Yada yada the flag is:
> CTF{Y0ur_Pr0ject'5_50urce_C0de_15_Le@ked}

___
___

**[50 POINTS]** *THE APOCALYPSE*

How the hell did they get a shell?
___

After a long unzip we get a file named `stage4.mem`

Using `binwalk` on it reveals a load of files...

I googled what is a `.mem` file and found the program named `volatility`. 

Trying to understand it for quite a while I gave up and tried common stego techniques like opening the file in a hex editor. 

After looking inside I found that there were strings I could read and that birthed the idea of using `strings` with `grep` on the file.

I'm not sure what was the intended solution but using 
> strings stage4.mem | grep CTF

I got the following output:

```
Found TESTINJECTFLAG
MSCTF.DLL
MSCTF.dll
MSCTF.DLL
MSCTF.dll
ICTFStateSink
CTF{1_F0UND Y0U L@P5U5$}.txt.lnk
MSCTF.dll
?bInit@BEZIER32@@QEAAHPEAU_POINTFIX@@PEAU_RECTFX@@@Z
MSCTF.dll
MSCTF.dll
CThreadMgrEventSink_DIMCallBack::CTFDetection. EnableSystemKeystrokeFeed==NULL
CThreadMgrEventSink_DIMCallBack::CTFDetection. DisableSystemKeystrokeFeed==NULL
MN_SELECTFIRSTVALIDITEM
MSCTF
MSCTF
?vInit@BEZIER64@@QEAAXPEAU_POINTFIX@@PEAU_RECTFX@@PEB_J@Z
?bInit@BEZIER32@@QEAAHPEAU_POINTFIX@@PEAU_RECTFX@@@Z
```

and adding underscores to this string gave me the right flag:

> CTF{1_F0UND_Y0U_L@P5U5$}

Lucky me :D




