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
    
    def __repr__(self):
        """Obyekt haqida malumot"""
        return f"Avto {self.rang} {self.make} {self.model}"

    def __eq__(self, boshqa_avto):
        """Tenglik"""
        return self.narx == boshqa_avto.narx

    def __lt__(self, boshqa_avto):
        """Kichik"""
        return self.narx < boshqa_avto.narx

    def __le__(self, boshqa_avto):
        """kichik yoki teng"""
        return self.narx <= boshqa_avto.narx


avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
avto4 = Avto("Mazda", "6", "Qizil", 2015, 35000)
#print(avto1 != avto2)

class Avtosalon:
    """Avtosalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosalon1"

    def add_avto(self, avto):
        if isinstance(avto, Avto):
            self.avtolar.append(avto)
        else:
            print("Avto obyektni kiriting")
    
    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Avto):
            self.avtolar[index]=value
            print(f"Ro'yxat o'zgardi")

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")

    def __add__(self, qiymat):
        if isinstance(qiymat, Avtosalon):
            yangi_salon = Avtosalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat, Avto):
            self.add_avto(qiymat)
        else:
            print(f"Avtosalonga {type(qiymat)} qo'shib bo'lmaydi")

    def __sub__(self, qiymat):
        if isinstance(qiymat, Avtosalon):
            yangi_salon = Avtosalon("Yangi salon")
            yangi_salon.avtolar = [x for x in self.avtolar if not x in qiymat.avtolar]
            return yangi_salon

    def __call__(self, *param):
        if param:
            for avto in param:
                self.add_avto(avto)
            print ([avto for avto in self.avtolar])
        else:
            print ([avto for avto in self.avtolar])

salon1 = Avtosalon("MaxAvto")
salon2 = Avtosalon("Avto Lider")
avto1 = Avto("GM", "Malibu", "Qora", 2020, 40000)
avto2 = Avto("GM", "Lacetti", "Oq", 2020, 20000)
avto3 = Avto("Toyota", "Carolla", "Silver", 2018, 45000)
avto4 = Avto("Mazda", "6", "Qizil", 2015, 35000)
avto5 = Avto("Volkswagen", "Polo", "Qora", 2017, 42000)
avto6 = Avto("Honda", "Accord", "Oq", 2017, 42000)
avto7 = Avto("BMW", 'X7', 'Qora', 2015, 75000)

salon1.add_avto(avto1, avto2, avto3)
salon2.add_avto(avto4, avto5, avto6)

salon3 = salon1 + salon2
salon4 = salon3 - salon2

salon1()
#salon4(avto7)


