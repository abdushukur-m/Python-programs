ismlar = ['Vali', 'Ali', 'Husan', 'Hasan', 'Ivan']
n=0
print("Bizda quyidagi ismlar mavjud: \n")

for ism in ismlar:
    print(ism)
    n=n+1
print(f"\nKod {n} marta takrorlandi!\n") 

sonlar=list(range(11,100,2))
kublar=[]

for son in sonlar:
    kublar.append({son**3})
print(sonlar)
print(kublar)

kinolar=[]

print("\nYoqtirgan 5 ta kino nomini kiriting: ")
for n in range(1,6):
    kinolar.append(input(f"{n}-kino: "))
print(kinolar)

tanishlar=[]
print(ismlar)
n=input("\nBu insonlardan necha kishini taniysiz: ")

for a in range(0, int(n)):
    tanishlar.append(input(f"{a+1}-inson: "))
print("\nSiz taniydigan odamlar", tanishlar)