toys = ('bus', 'car', 'bear', 'dino', 'snake', 'snake', 'lizard') #create a tuple
print(toys)
toys = list(toys[:]) # converting the tuple to a list
print(toys)

toys.append('dragon')
print(toys)

toys.remove('bus')
print(toys)

del toys[3]
print(toys)
