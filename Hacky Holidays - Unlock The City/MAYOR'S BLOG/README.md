# MAYOR'S BLOG - writeup
**[10 POINTS]** *FIND HIDDEN FLAG*

There is a hidden flag in the webpage. Can you find it?
___
After looking at the sources and finding nothing I decided to open up BurpSuite and just looking at the responses from the webpage and can notice the flag for the '/' get request:

![img0](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img0.png)

> CTF{xjDmWhLh3VHKip8NHYLRwbgoXmwaq5RG}

___
___

**[20 POINTS]** *GET ACCESS TO AN EDITOR ACCOUNT*

Try to exploit the password resetting functionality to gain access to an account.
___
I clicked on the login button and it brought to a standard login screen with a 
username and password.

There was a "forgot password" option. When you click it, you get brought to this page:

![img1](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img1.png)

and so I looked at the main page again to find the details, 

From this picture we can deduce the mayors friends name is George ✅

![img2](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img2.png)

The articals on this page are posted by "the_mayor" so its probably his username and in this picture, we learn that his birthday was on the 23rd of janurary 1972

![img3](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img3.png)

So if we enter the following information:

![img4](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img4.png)

We click reset password and we get the flag:

![img5](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img5.png)
> CTF{WwaqDNNkpPaGKKgJsAd71B5oP8TANyWl}

___
___

**[30 POINTS]** *ESCALATE TO ADMINISTRATIVE PRIVILEGES*

It looks like the design of the authentication system is very flawed. Find out how users are authenticated and exploit the system to gain Administrator rights.
___
We got the password for the mayors account 
> REFIeZnN8lrU6pLA

So we'll use it to access his account.
Using BurpSuite, if we just refresh the page we can intercept the get request 

![img6](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img6.png)

and modify the `isAdmin` cookie to True.

We get an option to `Check ngnix logs` and once we click it we get brought to this page with the password
> CTF{np3QKOEmYBJNcDaFuo3dcZQ8D1Pbeh4G}

![img7](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img7.png)

___
___

**[30 POINTS]** *GAIN ACCESS TO THE DEVELOPER CONSOLE*

There is special console for administrators on the website, but the link is hidden. Find the link, and gain relevant information from the logs. In the end, use the console to find user information.
___
Scrolling throught the logs we could see get requests to `robots.txt` and `admin_shell` and later in the logs we can see logs from a different IP. One interesting log was: 
`
      127.0.0.1 - - [26/Jun/2022:11:20:31 -0700] "GET /logging_in?username=sysadmin&password=JK28Qgb4WA3uuYa4 HTTP/1.1" 302 208 "http://mayorblog.local/login" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"
`

So, I tried loggin in as the sysadmin acount with `username=sysadmin password=JK28Qgb4WA3uuYa4` and then I tried to access the `robots.txt` file, it ended up redirecting to `admin_shell`. 

Accessing the admin_shell brought to a console like this:

![img8](https://github.com/LeonGurin/Hacky-Holidays-Unlock-the-City-Writeup/blob/main/MAYOR'S%20BLOG/images/img8.png)

entering `ls` and catting the file `user.txt` gets us the flag:
> CTF{3kdN6P8sEBLJyxHwsQlEgWVY2g3BBfan}

___
___

**[35 POINTS]** *CRACK THE PASSWORD OF THE ADMIN ACCOUNT ON THE SERVER* 
Find a vulnerability in the developer console and use it to access a password file.
___

🤷‍♂️
