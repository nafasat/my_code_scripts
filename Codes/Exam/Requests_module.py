#!/usr/bin/python3
import requests

r = requests.get('http://www.magicbricks.com')
print(r.status_code)