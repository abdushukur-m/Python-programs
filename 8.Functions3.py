def avto_info(make, model, rang, korobka, yil, narx=None):
    avto = {
        'kompaniya':make,
        'rang':rang,
        'model':model,
        'korobka':korobka,
        'yil':yil,
        'narx':narx
    }
    return avto
print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []

while True:
    print("\nQuyidagi ma'lmotlarni kiriting")
    kompaniya = input("Ishlab chiqaruvchi: ")
    rangi = input("Rangi: ")
    model = input("Modeli: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narxi = input("Narxi: ")
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))

    javob = input("Yana avto qo'shasizmi? (yes/no)")
    if javob == 'no':
        break
print("Onlayn bozordagi mavjud avtomashinalar: ")
for avto in avtolar:
    print(f"{avto['rang']} {avto['model']}. Narx: {avto['narx']}")