class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.name=ism
        self.surName=familiya
        self.year=tyil
    def get_name(self):
        return self.name
    
    def get_age(self, yil):
        return yil - self.year

    def tanishtir(self):
        return f"Ismim {self.name} {self.surName}, tug'ilgan yilim {self.year}"
    
talaba1 = Talaba("Hasan", "Olimov", 2000)
talaba2 = Talaba("Anvar", "Akromov", 2005)

print(talaba1.get_age(2022))

print(talaba1.tanishtir())
print(talaba2.get_name())
