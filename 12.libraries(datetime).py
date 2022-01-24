import datetime as dt

hozir = dt.datetime.now()
print(hozir)
#print(type(hozir))
print(hozir.date())
print(hozir.time())
print(hozir.hour)
print(hozir.minute)
print(hozir.second)

bugun = dt.date.today()
#print(f"Bugungi sana {bugun}.")

ertaga = dt.date(2022, 1, 24)
#print(f"Ertangi sana {ertaga}.")

hozir = dt.datetime.now()
vaqtHozir = hozir.time()

#print(f"Hozir soat {vaqtHozir}.")
#print(f"Hozir soat {hozir.hour}:{hozir.minute}.")

vaqtKeyin = dt.time(23, 30, 45)
#print(vaqtKeyin)

bugun = dt.date.today()
ramazon = dt.date(2022, 4, 1)

farq = ramazon - bugun

#print(f"Ramazonga {farq.days} kun qoldi.")

