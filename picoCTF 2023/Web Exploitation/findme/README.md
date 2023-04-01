# findme

**100 points**

Help us test the form by submiting the username as test and password as test!

*Note:* This challenge launches an instance on demand.

___

Welp I'm not sure what's happening but I did solve this.

I used `Burpsuite` to intercept the connection and see stuff I shouldn't.

When entering the credentials `test` and `test!` I had to forward different requests and there where two `sus` requests:

```
GET /next-page/id=cGljb0NURntwcm94aWVzX2Fs HTTP/1.1
GET /next-page/id=bF90aGVfd2F5X2RmNDRjOTRjfQ== HTTP/1.1
```

I decrypted the `ids` from base64 which gave the two parts of the flag that when combined gave me:

> picoCTF{proxies_all_the_way_df44c94c}
