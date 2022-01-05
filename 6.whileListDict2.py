cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'malibu', 'nexia', 'nexia']
print(f"Before removing similar elements: {cars}")
while 'nexia' in cars:
    cars.remove('nexia')
print(f"After removing similar elements: {cars}")
