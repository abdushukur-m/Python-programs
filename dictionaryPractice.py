davlatlar = {
    'afghanistan':'kabul',
    'albania':'tirana',
    'algeria':'algiers',
    'australia':'canberra',
    'austria':'vienna',
    'azerbaijan':'baku',
    'belarus':'minsk'
    }

print(f"Quyida {len(davlatlar)} ta davlatning nomlari: ")
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())

print(f"Quyida esa yuqoridagi {len(davlatlar)} ta davlatning poytaxtlari: ")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

print(f"Quyida {len(davlatlar)} ta davlat va ularning {len(davlatlar)} ta poytaxtlari:")
for davlat, poytaxt in sorted(davlatlar.items()):
    print(f"{davlat.title()}ning poytaxti {poytaxt.title()}")