import json

x = 10
x_json = json.dumps(x)

ism = 'anvar'
ism_json = json.dumps(ism)

sonlar = (12, 45, 23, 67)
sonlar_json = json.dumps(sonlar)

#print(sonlar)
#print(type(sonlar))
#print(sonlar_json)
#print(type(sonlar_json))

#print((json.loads(sonlar_json)))
#print(type(json.loads(sonlar_json)))

bemor = {
    'ism': "Alijon Valiyev",
    'yosh': 30,
    "oila":True,
    'farzandlar':("Ahmad", "Bonu"),
    "allergiya":None,
    "dorilar":[
        {"nomi":"Alangin", "miqdori":0.5},
        {"nomi":"Panadol", "miqdori":1.2}
    ]
}
#bemor_json = json.dumps(bemor)
#print(bemor_json)

bemor_json = json.dumps(bemor, indent=4)
#print(bemor_json)
#print(bemor.keys())
#print(bemor["dorilar"])

with open('sonlar.json', 'w') as f:
    json.dump(sonlar, f)

bemor2 = json.loads(bemor_json)
#print(type(bemor2))

sonlar2 = json.loads(sonlar_json)
#print(sonlar2[2])

with open('bemor.json') as f:
    bemor = json.load(f)

print(type(bemor))