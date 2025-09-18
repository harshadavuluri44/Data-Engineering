data = '{"employees":[{"name":"Alice","dept":"HR"},{"name":"Bob","dept":"IT"},{"name":"Charlie","dept":"Finance"}]}'

import json

parsed = json.loads(data)

val = parsed['employees']
result=[]

for x in val:
    result.append(x['name'])

print(result)
