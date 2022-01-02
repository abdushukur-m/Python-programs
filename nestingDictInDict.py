hamkasblar = {
    'ali':{'familya':'valiyev', 
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['pyhton', 'c++']w
           },
    'vali':{'familya':'aliyev', 
           'tyil':2001,
           'malumot':"o'rta maxsus",
           'tillar':['html','css', 'js']
           },
    'hasan':{'familya':'husanov', 
           'tyil':1999,
           'malumot':'maxsus',
           'tillar':['pyhton', 'php']
           }
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan.\n"
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi: ")
    for til in info['tillar']:
        print(f"{til.upper()}", end=' ')

    
