car0 = {
    'model':'lacetti', 'rang':'oq',
    'yil':2018, 'narx':13000,
    'km':50000, 'korobka':'avtomat'
}

car1 = {
    'model':'nexia 3', 'rang':'qora',
    'yil':2015, 'narx':9000,
    'km':89000, 'korobka':'mexanika'
}

car2 = {
    'model':'gentra', 'rang':'qizil',
    'yil':2019, 'narx':15000,
    'km':20000, 'korobka':'mexanika'
}

cars = [car0, car1, car2] #list of dictionaries

#for car in cars:
#    print(f"{car['model'].title()}, "
#          f"{car['rang'].title()}, "
#          f"{car['yil']} - yil, {car['narx']}$"
#    )

#print(cars[0])
#print(f"{cars[2]['rang'].title()} "
#      f"{cars[2]['model']}")

malibus = [] # a new list
for n in range(10):
    new_car = { # creating a dict
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narx':None,
        'km':0,
        'korobka':'avto'
    }
    malibus.append(new_car) #adding the dict to the list

for malibu in malibus[:3]:
    malibu['rang']='qizil'

for malibu in malibus[3:6]:
    malibu['rang']='qora'

for malibu in malibus[6:]:
    malibu['rang']='qora'
    malibu['korobka']='mexanika'

for malibu in malibus:
    if malibu['korobka']=='avto':
        malibu['narx']=40000
    else:
        malibu['narx']=35000

for malibu in malibus:
    print(malibu.values()) 
