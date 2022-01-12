import random as r

nums = r.sample(range(100), 10)
print(nums)

def isEven(x):
    """if x is even return True, otherwise return Odd"""
    return x%2==0

evenNums = list(filter(isEven, nums))
print(evenNums)

oddNums = list(filter(lambda x: x%2!=0, nums))
print(oddNums)


fruits = ['apple', 'banana', 'apricot', 'avocado', 'grapes', 'lemon']
fruitA = list(filter(lambda fruit: fruit.startswith('a'), fruits))
fruit4 = list(filter(lambda fruit: len(fruit)<=5, fruits))

print(fruits)
print(fruitA)
print(fruit4)

