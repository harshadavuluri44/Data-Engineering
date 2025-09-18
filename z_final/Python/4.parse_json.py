import json
with open('data/a.json', mode='r') as content:
    r = json.load(content)

    val = r['employees']
    
    result=[]

    for x in val:
        result.append(x['name'])

    print(result)


# json.load() -> is used to read json file object
# json.loads() -> is used to read json string