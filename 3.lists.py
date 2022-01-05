mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]

print("Birinchi meva: ", mevalar[0].upper())
print("Ikkinchi meva: ", mevalar[1].title())
print("Oxirgi meva: ", mevalar[-1])

print(mevalar)

mevalar.append("uzum") #add a new element to the list

print(mevalar)

mevalar.insert(0, 'nok') #add a new element to the index 0

print(mevalar)

del mevalar[1] #delete a list element using its index

print(mevalar)

mevalar.remove('uzum') #delete a list element using its value

print(mevalar)

mahsulot = mevalar.pop(1)
print("Men bozordan " + mahsulot + ' sotib oldim')
print("Olinmagan mevalar: ", mevalar)
