talabalar = ['hasan', 'husan', 'olim', 'botir']
boholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = int(input(f"{talaba.title()}ning bahosini kiriting: "))
    print(f"{talaba.title()} baholandi")
    boholangan_talabalar[talaba] = baho

print(boholangan_talabalar)
