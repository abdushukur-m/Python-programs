country = ['The USA', 'UZB', 'Germany', 'Russia', 'The UK', 'Australia']

print("Not sorted list : ", country)
print("The length of the list 'country' : ", len(country))

print("Sorted list A-Z: ", sorted(country))
print("Sorted list Z-A: ", sorted(country, reverse=True))

country.sort()
print("Sorted A-Z and saved list : ", country)

country.reverse()
print("Sorted Z-A and saved list : ", country)

country.remove("The UK")
print("After removing 'The UK' : ", country)

country.append("The UK")
print("After appending 'The UK' : ", country)

country.insert(0, "The UK")
print("After inserting 'The UK' on position 0 : ", country)

del country[0]
print("After deleting 0th element : ", country)

myCountry=country.pop(0)
print("I live in " + myCountry)
print("I dont live in these countries : ", country)


country=tuple(country)
print("After converting list to tuple : ", country)
