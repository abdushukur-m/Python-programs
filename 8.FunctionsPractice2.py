#1
from os import RTLD_DEEPBIND, pipe, pread


def foydalanuvchi_kirit(ismi, familyasi, yoshi, joyi, tnomeri=None, emanzili=None):
    foydalanuchi = {
        'ism':ismi,
        'familya':familyasi,
        'yosh':yoshi,
        'joy':joyi,
        'tnomer':tnomeri,
        'emanzil':emanzili
    }
    return foydalanuchi

foydalanuvchilar = []
#while True:
#    ismi = input("Ism kiting: ")
#    familyasi = input("Familya kiriting: ")
#    yoshi = input("Yosh kiriting: ")
#    joyi = input("Tug'ilgan joyni kiriting: ")
#    tnomeri = input("Telefon nomer kiriting: ")
#    emanzili = input("Elektron manzil kiriting: ")

#    foydalanuvchilar.append(foydalanuvchi_kirit(ismi, familyasi, yoshi, joyi, tnomeri, emanzili))
#    javob = input("Yana boshqa foydalanuvchi qo'shasizmi? (ha/yo'q)")
#    if javob != 'ha':
#        break

#print(foydalanuvchilar)
#foydalanuvchilar.append(foydalanuvchi_kirit('Alex', 'Bold', 18, 'Samarqand', '3959398', 'abdushukur771@mail.ru'))

#3

def katta_kichik(son1, son2, son3):

    if son1 >= son2:
        if son1 > son3:
            return son1
        else:
            return son3
    elif son2 >= son3:
        if son2 > son1:
            return son2
        else:
            return son1
    elif son3 >= son1:
        if son3 > son2:
            return son3
        else:
            return son2
    elif son1 == son2 and son1 == son3:
        return son1

while True:
    #s1 = int(input("1-chi son: "))
    #s2 = int(input("2-chi son: "))
    #s3 = int(input("3-chi son: "))
    
    #print(katta_kichik(s1, s2, s3))

    #javob = input("Yana ishlatasizmi? (ha/yo'q)")
    #if javob != 'ha':
        break 

#4
PI = 3.14
def aylana_haqida(radius):
    aylana = {
        'radius':radius,
        'diameter':(radius*2),
        'yuza':(PI*(radius**2)),
        'uzunlik':(2*PI*radius)
    }
    return aylana
print(aylana_haqida(2))

#5

def tub_sonlar(son1, son2):
    n = 1
    


