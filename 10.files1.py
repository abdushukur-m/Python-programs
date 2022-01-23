f_name = '/home/abdushukur/Documents/pi.txt'

with open(f_name) as file:
    pi = file.read()

print(pi)

pi = pi.rstrip()
#print(pi)

pi = pi.replace('\n', '')
#print(pi)

with open('talabalar.txt') as file:
    for line in file:
        print(line)

with open('talabalar.txt') as file:
        talabalar = file.readlines()
print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)
