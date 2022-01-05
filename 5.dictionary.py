car = {
    'make':'GM',
    'model':'Malibu',
    'color':'Black',
    'gear':'Automatic',
    'year':2020,
    #'price':40000
}
#print(f"Before adding a new element: {car}")
car['price']=40000
#print(f"After adding a new element: {car}")
#talaba = {}
#print(talaba)

#if 'price' in car:
#    print(car['price'])

#print(car.items()) # using .itmes() method
#for kalit, qiymat in car.items():
    #print(f"Kalit: '{kalit}'")
    #print(f"Qiymat: '{qiymat}'")

#for key in car:
for key in car.keys():
    print(key)
for value in car.values():
    print(value)

