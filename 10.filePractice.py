#2

filename = '/home/abdushukur/Documents/pi.txt'

with open(filename) as file:
    pi = file.read()
    bday = 25022000
    bday = str(bday)

    if bday in pi:
        print("Exists")
    else:
        print("Does not exist")

#3
