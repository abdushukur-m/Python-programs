#importing math module
import math
from math import atanh, e, pi #importing exp, pi

x = 400
print(math.sqrt(x))
print(math.pow(20, 2))

print(e)
print(pi)

print(math.log2(4))
print(math.log10(100))

#importing random module
import random as r # importing random module as r
son = r.randint(0, 100)
print(son)

ismlar = ['olim', 'hasan', 'husan', 'anvar']
ism = r.choice(ismlar)
print(ism.title())

x = list(range(0, 51, 5))
print(x)
print(r.choice(x))
r.shuffle(x)
print(x)

y = r.sample(x, k=3)
print(y)

