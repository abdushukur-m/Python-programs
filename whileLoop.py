son = 5

while son>=1:
#    print(son, end=' ')
    son-=1

print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
savol = "Istalgan son kiriting "
savol += "(To'xtatish uchun 'exit deb yozing): "
qiymat = ''
while qiymat!='exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)

        