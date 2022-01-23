class Car:
    """(self, make, model, year, km=0, price=None)"""
    def __init__(self, make, model, year, km=0, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.__km = km

    def set_price(self, price):
        self.price = price
    
    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            raise ValueError("Musbat son kiriting")

    def get_info(self):
        info = f"{self.make.upper()} {self.model.title()}, "
        info += f"{self.year}-yil, {self.__km}km yurgan."
        if self.price:
            info += f"Narxi: {self.price}"
        return info

    def get_km(self):
        return self.__km

#avto1 = Car('gm', 'malibu', 2020)
#print(avto1.get_info())
#avto1.add_km(5000)
#print(avto1.get_km())
#avto1.add_km(-4500)