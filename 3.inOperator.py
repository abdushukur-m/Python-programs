menyu = ['osh', 'manti', 'shashlik', 'norin', 'somsa', 'qozonkabob']
#'manti' in menyu

ovqat = input("Nima ovqat yeysiz?>>>")
if ovqat.lower() in menyu:
    print("\nBuyurtma qabul qilindi. ")
else: 
    print("\nAfsuski bizda bunday ovqat yo'q")

if ovqat.lower() not in menyu:
    print("\nAfsuski bizda bunday ovqat yo'q")
else: 
    print("\nBuyurtma qabul qilindi. ")