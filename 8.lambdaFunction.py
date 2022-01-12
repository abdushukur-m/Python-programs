import math

length = lambda pi, r : 2*pi*r
#print(length(math.pi, 10))

def power(n):
    return lambda x : x**n 

square = power(2)
cube = power(3)

print(f"3 squared is equal to {square(3)}")
print(f"3 cubed is equal to {cube(3)}")

