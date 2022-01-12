from math import sqrt
import math

nums = list(range(11))
sqroots = list(map(sqrt, nums))

print(nums)
print(sqroots)

def power2(x):
    return x*x
print(list(map(power2, nums)))

print(list(map(lambda x: x*x, nums)))

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x, y: x+y, a, b))

print(a_plus_b)

names = ['hasan', 'husan', 'anvar', 'olim']

print(list(map(lambda name: name.title(), names)))
