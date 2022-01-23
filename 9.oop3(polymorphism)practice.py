class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
inson = Shaxs("Abdushukur", "Mukhiddinov", "AA1234567", 1998)
#print(f"{inson.get_info()}. {inson.get_age(2022)} yoshda.")


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, id, manzil):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = id
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
    
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida malumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID: {self.idraqam}"
        return info

    def fanga_yozil(self, fan):
        """Talabani fanlar ro'yxatiga qo'shish"""
        self.fanlar.append(fan)

    def get_fanlar(self):
        """Fanlar ro'yxatini qaytaruvchi metod"""
        return [x.get_subname() for x in self.fanlar]

    def remove_fan(self, fan):
        removed = True
        """Fanlar ro'yxatidan fanni o'chiruvchi metod"""
        for x in self.fanlar:
            if fan == x.get_subname():
                self.fanlar.remove(x)
                removed = False
                print(f"{fan} muvaffaqiyatli o'chirildi")
        if removed:
            print("Siz bu fanga yozilmagansiz")

class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy
        self.kocha= kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

manzil = Manzil(36, 'Registon', 'Urgut', 'Samarqand')
talaba1 = Talaba("Abdushukur", "Mukhiddinov", "AA1234567", 1998, "0000012", manzil)
#print(talaba.get_info())
#print(talaba.get_age(2022))

#print(f"{talaba.get_info()}. ID:{talaba.get_id()}")
#print(f"{talaba.get_bosqich()}-bosqich talabasi")
#print(talaba.get_info())
#print(talaba.manzil.get_manzil())

class Fan:
    """Fan nomi class yaratildi"""
    def __init__(self, fnomi, daraja, darslik):
        """Fanning xususiyatlari"""
        self.fnomi = fnomi
        self.daraja = daraja
        self.darslik = darslik
    def get_subname(self):
        """fanning nomi qaytaradigan method"""
        return self.fnomi
    def get_daraja(self):
        """fanning darajasini qaytaradigan method"""
        return self.daraja
    def get_darslik(self):
        """fanning darsligini qaytaradigan method"""
        return self.darslik

fan1 = Fan("Oliy Matematika", "yuqori", "Oliy matematika darsligi")
fan2 = Fan("Python", "boshlang'ich", "Python asoslari")
#print((fan1.get_daraja()).title())
talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
#print(talaba1.get_fanlar())
#talaba1.remove_fan("Math")

class Foydalanuvchi(Shaxs):
    """Foydalanuvchi nomli voris klass yaratildi"""
    def __init__(self, ism, familiya, passport, tyil, username, idraqam):
        super().__init__(ism, familiya, passport, tyil)
        """Foydalanuvchining qo'shimcha xususiyatlari"""
        self.idraqam = idraqam
        self.username = username
        self.foydalanuvchi_dict = {
            self.username:[self.ism, self.familiya, self.tyil, self.idraqam]
        }

    def get_id(self):
        """Foydalanuvchi ID #ni qaytaruvchi metod"""
        return self.idraqam
    
    def get_username(self):
        """Foydalanuvchi Username ini qaytaruvchi metod"""
        return self.username

    def get_info(self):
        """Foydalanuvchi ism, familiyasini qaytaruvchi metod"""
        return self.foydalanuvchi_dict.values()

    def update_info(self, old_username, new_username):
        """Foydalanuvchi Username ini o'zgartiruvchi metod"""
        if old_username in self.foydalanuvchi_dict.keys():
            self.username = new_username
            print(f"{old_username} {new_username}ga o'zgartirildi")
        else:
            print("Bunday Username mavjud emas")
    
foydalanuvchi1 = Foydalanuvchi("Abdushukur", "Mukhiddinov", "AB2500837", "1998", "bigbrother_1", "001")
#print(foydalanuvchi1.get_info())
#print(foydalanuvchi1.get_username())
#foydalanuvchi1.update_info("bigbrother_1", "daffodil")
#print(foydalanuvchi1.get_username())

class Admin(Foydalanuvchi):
    """Admin nomli voris klass yaratildi"""
    def __init__(self, ism, familiya, passport, tyil, username, idraqam):
        super().__init__(ism, familiya, passport, tyil, username, idraqam)
        self.parol = 12345 #admin foydalanuvchilarni bloklashi uchun to'g'ri parolni kiritishi lozim

    def ban_user(self, user):
        parol=int(input("Parolni kiriting: "))
        if parol == self.parol:
            print(f"{user} bloklandi")
        else:
            print(f"Noto'g'ri parol kiritildi. To'g'ri parol {self.parol}")

    
admin = Admin("Alex", "Bold", passport=None, tyil=None, username=None, idraqam=None)
admin.ban_user("bigbrother_1")












