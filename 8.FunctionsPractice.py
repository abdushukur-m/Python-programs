#1
def tYil_hisobla(ism, yosh):
    print(f"{ism.title()}, siz {2022-yosh}-yilda tug'ilgansiz ")

tYil_hisobla(yosh=24, ism='abdushukur')

#2
def darajaHisobla(son):
    print(f"{son} ning kvadrati - {son**2}, kubi - {son**3}")
darajaHisobla(7)

#3
def jufttoqAniqla(son):
    print(f"{son} - juft son") if son%2==0 else print(f"{son} - toq son")
jufttoqAniqla(75)

#4
def kattaKichik(son1, son2):
    if son1>son2:
        print(f"{son1} > {son2}")
    elif son1<son2:
        print(f"{son1} < {son2}")
    else:
        print(f"{son1} va {son2} lar teng")
kattaKichik(7, 50)

#5
def daraja_aniqla(son, daraja):
    print(f"{son} ning {daraja}-darajasi - {son**(daraja)}")
daraja_aniqla(7, 5)

#6
def daraja_aniqla(son, daraja=2):
    print(f"{son} ning {daraja}-darajasi - {son**(daraja)}")
daraja_aniqla(7)

#7
def bolinishni_tekshir(son):
    for n in range(2, 11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")
bolinishni_tekshir(20)


