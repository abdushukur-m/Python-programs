def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi

print(summa(1, 2, 3))

def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
    return sum(sonlar)

print(summa(1, 2, 3))

def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini qaytaruvchi funksiya"""
    return x+y+sum(sonlar)

#print(summa(1))
print(summa(1, 2))
print(summa(1, 2, 3))

def kopaytma(*sonlar):
    """Kiritilgan sonlar ko'paytmasini qaytaruvchi funksiya"""
    kop=1
    for son in sonlar:
        kop *= son
    return kop
print(kopaytma(1, 2, 3, 4))