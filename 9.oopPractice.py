class UserDefine:
    """web user class"""
    def __init__(self, name, surname, age, country, language):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.language = language
    def introduce(self):
        return(f"I'm {self.name} {self.surname} and {self.age}. I speak in {self.language} and I'm from {self.country}")
    def printName(self):
        return self.name
    def printSurname(self):
        return self.surname
    def printAge(self):
        return self.age
    def printLanguage(self):
        return self.language
    def printCountry(self):
        return self.country
    def printEmail(self, mail):
        return mail

#name = input("Name: ")
#surname = input("Surname: ")
#age = input("Age: ")
#country = input("Country: ")
#language = input("Language: ")

#user1 = UserDefine(name, surname, age, country, language) 
user1 = UserDefine("Alex", "Bold", 24, 'Uzbekistan', "Uzbek")
#print(user1.introduce())
print(user1.printEmail("alex@mail.ru"))


