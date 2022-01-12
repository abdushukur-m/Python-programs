#1

num = 17
num10 = lambda num: num*10

print(num10(num))

#2

num1 = 15
num2 = 25

sum = lambda x, y: x+y
print(sum(num1, num2))

#3

from math import trunc
from random import sample

nums = list(sample(range(1000), 10))

squared = list(map(lambda x: x*x, nums))
odds = list(filter(lambda x: x%2!=0, nums))

print(nums)
print(squared)
print(odds)

#4

nums = list(range(1, 10000))
def isPrime(x):
    m=0
    for n in range(1, x+1):
        if x%n == 0:
            m += 1
    return m==2
primeNums = list(filter(isPrime, nums))
print(primeNums)


