#1
shaxslar = {
    'shaxs1' : {
        'ism':'abdulla', 'familya':'oripov',
        'yyil':'1941-2016', 'asarlar':["jannatga yo'l", 'hakim va ajal', 'ranjkom']
        },

    'shaxs2' : {
        'ism':'mirkarim', 'familya':'osim',
        'yyil':'1907-1984', 'asarlar':["temur malik", 'mahmud torobiy']
        },

    'shaxs3' : {
        'ism':'muhammad', 'familya':'yusuf',
        'yyil':'1954-2001', 'asarlar':["iltijo", 'osmonimga olib ketaman', 'tanish teraklar']
        },

    'shaxs4' : {
        'ism':'abdulhamid', 'familya':"cho'lpon",
        'yyil':'1897-1938', 'asarlar':['qurboni jaholat']
        }
    }


#for info in shaxslar.values():
#    print(f"\n{info['ism'].title()} {info['familya'].title()}")
#    print(f"Yashagan yillari: {info['yyil']}")
#    print("Mashhur asarlari: ")
#    for asar in info['asarlar']:
#        print(asar.title())

#4

countries = {
    'ecuador':{
        'capital':'quito', 'language':'spanish',
        'currency':'US Dollar', 'religion':'christianity'
    },
    'El Salvador':{
        'capital':'sal salvador', 'language':'spanish',
        'currency':'US Dollar', 'religion':'christianity'
    },
    'indonesia':{
        'capital':'jakarta', 'language':'indonesian',
        'currency':'rupiah', 'religion':'islam'
    },
    'singapore':{
        'capital':'singapore', 'language':'malay',
        'currency':'singapore dollar', 'religion':'buddhist'
    }
}

for name, info in countries.items():
    print(f"Country: {name.title()}\nCapital: {info['capital'].title()}")
    print(f"Currency: {info['currency'].title()}\nLanguage: {info['language'].title()}\n")
