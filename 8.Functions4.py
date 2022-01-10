def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar)
#print(baholar)
print(bahola(talabalar[:]))
#print(bahola(talabalar))
#print(talabalar)

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"{ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar

talabalar = ['ali', 'vali', 'hasan', 'husan']
print(talabalar)
print(bahola(talabalar))