import json
#from googletrans import Translator

#tarjimon = Translator() #Translator - bu maxsus klass, tarjimon esa obyekt

#matn_uz = "Python - dunyodagi eng mashhur dasturlash tili"
#tarjima_eng = tarjimon.translate(matn_uz)
#print(tarjima_eng.text)

#tarjima_rus = tarjimon.translate(matn_uz, dest='ru')
#print(tarjima_rus.text)

#print((tarjimon.translate(tarjima_rus.text, dest='uz', src='ru').text))


import requests
from pprint import pprint

#sahifa = "https://kun.uz/news/main"
#r = requests.get(sahifa)
#pprint(r.text)

country = "Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json.keys())
# print(r_json['capital'])