#1
#yosh = int(input("Yoshingiz nechada: "))

#if yosh<=4:
    #print("Kirish bepul")
#elif yosh <= 18:
#    print("Kirish 10000 so'm")
#else:
#    print("Kirish 20000 so'm")
#2
#son1 = int(input("Birinchi son: "))
#son2 = int(input("Ikkinchi son: "))

#print(f"{son1}>{son2}") if son1>son2 else print(f"{son1}<{son2}")

#3,4
mahsulotlar = ['ruchka', 'qalam', 'daftar', 'kitob', 'sumka', 'qaychi', 'stol', 'stul', 'shisha', 'rang']
savat = []
bor_mahsulotlar = []
mavjud_emas = []

n=int(input("Nechta mahsulot olmoqchisiz?"))

for a in range(n):
    savat.append(input(f"{a+1}-mahsulot: "))
print(savat)

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)
else:
    print("Savat hali bo'sh")

if not mavjud_emas:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor\n", bor_mahsulotlar)
else:
    print("\nQuyidagi mahsulotlar do'konimizda yo'q\n", mavjud_emas)

#5
foydalanuvchilar = ['ali', 'vali', 'hasan', 'husan', 'ivan']
yangi_login = input("Login kiriting: ")

if yangi_login.lower() in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {yangi_login}")

