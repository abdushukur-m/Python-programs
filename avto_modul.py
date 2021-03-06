from uuid import uuid4

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    def get_km(self):
        return self.__km

    def add_km(self, km):
        """Mashinaning km ga km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")

    def get_id(self):
        return self.__id
    
    def set_id(self, newid):
        self.__id = newid

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto