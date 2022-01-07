def toliq_ism_yasa(ism, familiya, otasining_ismi = ''):
    """To'liq ism qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title() #returns a value

talaba1 = toliq_ism_yasa('abdushukur', 'mukhiddinov', "fozil o'g'li")
print(talaba1)

# dictionary returning function

def avto_info(make, model, rang, korobka, yil, narx=None): # narx is an optionalt standard parameter 
    avto = {'kompaniya':make,
            'model':model,
            'rang':rang,
            'korobka':korobka,
            'yil':yil,
            'narx':narx} 
    return avto

avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
avtolar = [avto1, avto2]
print("Onlayn bozordagi mavjud avtomashinalar: ")
for avto in avtolar:
    if avto['narx']:
        narx = avto['narx']
    else:
        narx = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narx: {narx}")

# list returning function
def oraliq(min, max):
    sonlar = [] # an empty list
    while min<max:
        sonlar.append(min)
        min += 1
    return sonlar

print(oraliq(0, 10))
print(oraliq(10, 21))

def oraliq(min, max, qadam=''): # optional standard parameter
    sonlar = []
    while min<max:
        if qadam:
            sonlar.append(min)
            min += qadam
        else:
            sonlar.append(min)
            min += 1
    return sonlar

print(oraliq(0, 10))
print(oraliq(0, 21, 2))

