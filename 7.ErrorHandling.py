#1
son = 45
#son = float(input("Juft son: "))
if son%2 != 0:
    print("Bu juft son emas. ")
else:
    print("Rahmamt! ")

#2
yosh = int(input("Yoshingizni kiriting: "))

if yosh<=4 or yosh >= 60:
    narx = 0
elif yosh < 18:
    narx = 10000
else:
    narx = 20000
print(f"Chipta {narx} so'm")