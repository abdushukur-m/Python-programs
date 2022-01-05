#yosh = input("Yoshingizni kiriting: ")
#try:
#    yosh = int(yosh)
#    print(f"Siz {2022-yosh} yilda tug'ilgansiz")
#except: 
#    print("Butun son kiritmadingiz")

#print("Dastur tugadi")

yosh = 78
#yosh = input("Yoshingizni kiriting: ")
try:
    yosh = int(yosh)
except ValueError: 
    print("Butun son kiritmadingiz")
else:
    print(f"Siz {2022-yosh} yilda tug'ilgansiz")
print("Dastur tugadi")

x, y = 5, 10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")

mevalar = ['olma', 'anor', 'amjir', 'uzum']
try:
    print(mevalar[7])
except IndexError:
    #print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")
    pass