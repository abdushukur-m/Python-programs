mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']

for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon},")
    print("Sizni 20-Mart kuni nahorgi oshga taklif qilamiz. ")
    print("Hurmat bilan, palonchiyevlar oilasi")

sonlar = list(range(1, 11))

for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
print("Dastur tugadi")

sonKvadrati=[]

for son in sonlar:
    sonKvadrati.append(son**2)
print(sonlar)
print(sonKvadrati)

dostlar=[]
print("5 ta eng yaqin do'stingiz kim?")

for n in range(1,6):
    dostlar.append(input(f"{n}-ismini kiriting: "))
print(dostlar)