#!/usr/bin/python3
import requests
import sys

try:
	File=open('/tmp/VIP.txt','r')
except Exception:
	print("Input File Error")
	sys.exit(1)

for VIP in File:
	VIP=VIP.strip()
	Query="http://192.168.33.212:5000/api/v0.1/getdnsmapping?ip="+VIP
	r = requests.get(Query)
	Data=r.json()
	Result=Data["result"]
	if 'not found' in Result:
		print(VIP,"\tdomains_not_Mapped")
	else:
		List=Result[VIP]
		Alldomain=[]
		for domains in List:
			map_domain=''.join(domains.keys())
			Alldomain.append(map_domain)
	
		print(VIP,"\t",Alldomain)

