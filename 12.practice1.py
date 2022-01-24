import datetime as dt

#1

bugun = dt.date.today()
#print(bugun)
farq = 14

for i in range(9):
    kun = bugun + dt.timedelta(days=farq)
#    print(kun) 
    farq += 14

#2

bugun = dt.date.today()

ramazon_hayit = dt.date(2022, 5, 3)
qurbon_hayit = dt.date(2022, 7, 10)

print(f"Ramazon hahyitgacha {(ramazon_hayit-bugun).days} kun qoldi.")
#print(f"Qurbon hayitgacha {qurbon_hayit-bugun}kun qoldi.")

#3

t_yil = dt.date(1998, 10, 30)
davr = (bugun-t_yil).days

#print(f"Tug'ilgan kunimdan bugungacha {((davr%365)%31)} kun, {(davr%365)//31} oy, {davr//365} yil o'tdi.")

import re

andoza = "^[\+]?[(]?[0-9]{4}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

ph_num1 = "+998943218718"
ph_num2 = "+99894-321-87-12"
ph_num3 = "998943218712"
ph_num4 = "(94) 321 87 12"
ph_num5 = "321-87-12"
ph_num6 = "321 87 12"
ph_num7 = "+(99894) 321 87 12"


print(re.match(andoza, ph_num1))
print(re.match(andoza, ph_num2))
print(re.match(andoza, ph_num3))
print(re.match(andoza, ph_num4))
print(re.match(andoza, ph_num5))
print(re.match(andoza, ph_num6))
print(re.match(andoza, ph_num7))





