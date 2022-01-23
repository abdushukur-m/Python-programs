import json
from textwrap import indent

data = {
    "model":"Malibu",
    "rang":"Qora",
    "yil":2020,
    "narx":40000
}

data_json = json.dumps(data, indent=4)
#print(data_json)

#print(data_json[12])
with open('data.json', 'w') as f1:
    json.dump(data_json, f1)

with open('data.json') as f1:
    data1=json.load(f1)


#print(type(data_json))
#print(type(data1))
data1 = json.loads(data1)
#print(type(data1))
#print(data_json)
#print(data1['model'])

talaba = {
    'ism':'Hasan',
    'familiya':'Husanov',
    'tyil':2000
}
talaba_json = json.dumps(talaba)

with open('talaba.json', 'w') as f2:
    json.dump(talaba_json, f2)

with open('talaba.json') as f2:
    talaba1 = json.load(f2)

#print(talaba1)

f_name = '/home/abdushukur/Downloads/api-result.json'

with open(f_name) as f3:
    info_json = json.load(f3)

info_json = json.dumps(info_json, indent=4)
#print(info_json)
#print(type(info_json))
info = json.loads(info_json)

#print(type(info))

print(info['query']['pages']['13801']['title'])
print(info['query']['pages']['13801']['extract'])
