#!/usr/bin/python3
import json

data = '{"name":"Nafasat Ahmed", "age": 25, "Cars": ["Ford","Alto"] }'

print(data)
json_data = json.loads(data)
print(json_data['Cars'])