A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
#C = A|B #merging 2 sets using |
C = A.union(B) #merging 2 sets using .union() method
print(C)

#D = A&B #finding similar elements of 2 sets using &
D = A.intersection(B) #finding similar elements of 2 sets using .intersection() method
print(D)

#finding different elements in 2 sets using - 
print(A-B)

#finding different elements in 2 sets using .difference() method
print(B.difference(A))

#finding symmetric difference between 2 sets using ^
print(A^B)

#finding symmetric difference between 2 sets using .symmetric_difference()
print(B.symmetric_difference(A))
