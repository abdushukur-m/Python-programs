def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompaniya']=kompaniya
    malumotlar['model']=model
    return malumotlar

avto1 = avto_info('GM', 'malibu', rang='qora', yil=2018)
avto2 = avto_info('Kia', 'K5', rang='qizil', narx=35000)
print(avto1)
print(avto2)

def talaba_info(ism, familiya, **malumotlar):
    """Talabalar haqida malumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1 = talaba_info('Alex', 'Bold', yosh=18)
talaba2 = talaba_info('Tom', 'Hardy', baho=5)
print(talaba1)
print(talaba2)


