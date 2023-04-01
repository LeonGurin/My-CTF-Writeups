# MatchTheRegex

**100 points**

AUTHOR: SUNDAY JACOB NWANYIM

Description
How about trying to match a regular expression
The website is running here.

*Note:* This challenge launches an instance on demand.

___

Looking inside the script tag we can see:

```html
<script>
	function send_request() {
		let val = document.getElementById("name").value;
		// ^p.....F!?
		fetch(`/flag?input=${val}`)
			.then(res => res.text())
			.then(res => {
				const res_json = JSON.parse(res);
				alert(res_json.flag)
				return false;
			})
		return false;
	}

</script>
```

The regex is supposed to be `^p.....F!?`, literally the first and only guess was `picoCTF`, when I entered it gave the flag:

> picoCTF{succ3ssfully_matchtheregex_08c310c6}
