ismlar = []
n = 1

print("Yaqin do'stlaringizni ismlarini kiriting: ")
while True:
    savol = f"{n}-do'stingizni ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana ism qo'shasizmi? (ha\yo'q)")
    if javob == 'ha':
        n+=1
        continue
    else:
        break
print("Ro'yxat tuzildi.")

print("Do'stlaringiz ro'yxati:")
for ism in sorted(ismlar):
    print(ism.title())