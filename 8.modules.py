import avto_info_mod

#avto1 = avto_info_mod.avto_info("GM", 'Malibu', 'Qora', "avtomat", 2020, 40000)
#avto_info_mod.info_print(avto1)

import avto_info_mod as aim

#avto1 = aim.avto_info("GM", 'Malibu', 'Qora', "avtomat", 2020, 40000)
#aim.info_print(avto1)

from avto_info_mod import avto_info, info_print, info_print

avto1 = avto_info("GM", 'Malibu', 'Qora', "avtomat", 2020, 40000)
info_print(avto1)
