fruits = ['pear', 'banana', 'apple', 'watermelon', 'lemon']
print("Elementlar soni: ", len(fruits)) # using len function

sonlar = list(range(0, 10)) # using list and range functions
print(sonlar)

juftSonlar = list(range(0, 20, 2))
print("Juft sonlar: ", juftSonlar)

toqSonlar = list(range(1, 20, 2))
print("Toq sonlar ", toqSonlar)

sonlar = list(range(10))
print(sonlar)

narxlar = [12000, 22500, 3000, 40000, 15000]
arzon = min(narxlar) # min function 
qimmat = max(narxlar) # max function
jami = sum(narxlar) # sum function
print("Eng arzon narx : ", arzon, "\nEng qimmat : ", qimmat, "\nJami : ", jami)

cars = ['bmw', 'volvo', 'gm', 'toyota', 'tesla', 'audi']
print("cars : ", cars) 
myCars = cars[0:3] # cutting list elements
print("myCars : ", myCars)

myCars2 = cars[:3]
print("myCars2 : ", myCars2)

myCars3 = cars[3:]
print("myCars3 : ", myCars3)