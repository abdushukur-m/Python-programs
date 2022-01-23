faylnomi = 'ustozlar.txt'
with open(faylnomi, 'w') as fayl:
    fayl.write('Hello world!'+'\n')
    fayl.write('This is a new file.')

with open(faylnomi, 'a') as fayl:
    fayl.write('\nAlijon Valiyver')

    