davlatlar = {
    'afghanistan':'kabul',
    'albania':'tirana',
    'algeria':'algiers',
    'australia':'canberra',
    'austria':'vienna',
    'azerbaijan':'baku',
    'belarus':'minsk'
    }

davlatNomi = input("Istalgan davlat nomini kiriting: ")

for davlat, poytaxt in davlatlar.items():
    if davlatNomi == davlat:
        print(poytaxt)
    else:
        print("Kechirasiz, bizda bunday ma'lumot yo'q")
