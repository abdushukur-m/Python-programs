narx = 15000
choy = True
salat = False

if choy and salat:
    narx = narx + 10000
elif choy or salat:
    narx = narx + 5000

print(f"Jami {narx} so'm!")  