#1
kitoblar = set()
kitob = ''

#while True:
#    kitob = input("Kitob nomini kiriting(To'xtatish uchun 'stop' kiriting): ")
#    if kitob == 'stop':
#        break
#    else:
#        kitoblar.add(kitob)

#print(kitoblar)

#2
savol = "Yoshingizni kiriting"
savol += "(To'xtatish uchun 'exit' yoki 'quit' kiriting):"
while True:
    yosh = input(savol)
    if yosh == 'exit' or yosh == 'quit':
        break
    else:
        yosh=int(yosh)
        if int(yosh) <= 7:
            narx = 2000
        elif yosh > 7 and yosh <= 18:
            narx = 3000
        elif yosh > 18 and yosh <=65:
            narx = 10000
        elif yosh > 65:
            narx = 0
        print(f"Sizning yoshingiz {yosh} da bo'lgani uchun chipta narxi {narx} so'm. ")
        break