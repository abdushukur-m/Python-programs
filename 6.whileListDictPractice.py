buyurtmalar = []
print("Mahsulotlar buyurtma qiling: ")

while True:
    buyurtma = input("to'xtatish uchun 'quit' yozing: ")
    if buyurtma != 'quit':
        buyurtmalar.append(buyurtma)
    else:
        break

e_bozor = {
    'olma':10000, 'uzum':15000,
    'anor':20000, 'anjir':30000,
    'non':3000
}
print(f"Yangi mahsulotlar qo'shishdan oldin: {e_bozor}")

while True:
    kalit = input("Mahsulot nomini kiriting (to'xtatish uchun 'quit' yozing): ")
    if kalit != 'quit':
        qiymat = input(f"{kalit} narxini kiriting: ")
        e_bozor[kalit]=qiymat
    else: 
        break
print(f"Yangi mahsulotlar qo'shgandan keyin: {e_bozor}")

    