#1
colors = {'red', 'white', 'yellow'}
#print(f"Original set: {colors}")

colors.add('green') #adding a new element using .add() method
#print(f"After adding a new element 'green' using .add(): {colors}")

colors.update(['black', 'purple', 'blue'])
#print(f"After adding a new element 'green' using .update(): {colors}")

#2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

#set3=set1&set2
set3=set1.intersection(set2)
#print(sorted(set3))

#print(set1-set2)
#print(set2.difference(set1))

#3
bozorlik = ['choy', 'non', 'tuxum', 'kartoshka', 'sut']
mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']

mavjud_mahsulot = []
mavjud_bolmagan = []

for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        mavjud_mahsulot.append(mahsulot)
    else:
        mavjud_bolmagan.append(mahsulot)

print("Before adding new elements:")
print(mavjud_mahsulot)

mahsulotlar.append('choy')
mahsulotlar.append('kartoshka')

print("After adding new elements:")
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        mavjud_mahsulot.append(mahsulot)
    else:
        mavjud_bolmagan.append(mahsulot)

print(set(mavjud_mahsulot))
