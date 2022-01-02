print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(To'xtatish uchun 'exit deb yozing): " 
flag=True

while flag:
    qiymat = input(savol)
    if qiymat == 'exit':
        flag = False
    else:
        print(float(qiymat)**2)