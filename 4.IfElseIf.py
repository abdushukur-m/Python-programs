yosh=int(input("Yoshingiz nechida: "))

if yosh<7:
    print("Sizga avtobus bepul\n")
else:
    print("Sizga avtobus pullik\n")

avtolar=['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    print(avto.upper()) if avto=='bmw' else print(avto.title())

cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    print(car.title()) if car!='gm' else print(car.upper())

print(78**0.5)

if yosh<=4:
    narx=0
elif yosh<=12:
    narx=5000
else:
    narx=10000
print(f"Siza kirish {narx} so'm!\n")

bugun=input("Bugun haftaning qaysi kuni: ")

if bugun.lower()=='chorshanba' and (yosh<7 or yosh>65): print("Bugun sizga muzeyga kirish bepul!\n")