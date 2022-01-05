def salomBer(ism): #defining a new funct called salomBer using def operator
    """Foydalanuvchi ismini qabul qilib,
    unga Salom beruvchi funksiya""" #docstring 
    print(f"Assalomu aleykum, hurmatli {ism.title()}!")
salomBer('hasan')
print(salomBer.__doc__)
salomBer(ism='olim')

def yoshHisobla(tYil, jYil=2022): #standard value to the parameter jYil
    print(f"Siz {jYil-tYil} yoshdasiz")
yoshHisobla(1998)


