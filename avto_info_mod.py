def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi}
    return avto

def avto_kirit():
    print("Saytimizdagi avtolar ro'yxatini shakllantiramiz: ")
    avtolar = []

    while True:
        print("Quyidagi ma'lumotlarni kiriting")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narxi = input("Narxi: ")

        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        javob = input("Yana avto qo'shasizmi? ha/yo'q ")
        if javob != 'ha':
            break

def info_print(avto_info):
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")


