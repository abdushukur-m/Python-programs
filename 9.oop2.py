class Student:
    """Student nomli class yaratamiz"""
    def __init__(self, ism, familiya, tyil):
        """Studentning xususiyatlari"""
        self.name = ism
        self.surname = familiya
        self.year = tyil
        self.grade = 1

    def set_grade(self, bosqich):
        """Student kursini yangilovchi metod"""
        self.grade = bosqich
    
    def udpate_grade(self):
        """Studentning bosqichini 1 taga ko'paytiruvchi metod"""
        self.grade += 1
    
    def get_info(self):
        """Student haqida ma'lumot qaytaruvchi metod"""
        return f"{self.name} {self.surname}, {self.grade}-year student"
    
    def get_name(self):
        """Studentning ismini qaytaruvchi metod"""
        return self.name
    
    def get_lastname(self):
        """Studentning familiyasini qaytaruvchi metod"""
        return self.surname
    
    def get_fullname(self):
        """Studentning to'liq ismini qaytaruvchi metod"""
        return f"{self.name} {self.surname}"
    
    def get_age(self, yil):
        """Studentning yoshini qaytaruvchi metod"""
        return yil-self.year
    
class Subject:
    """Subject nomli class"""
    def __init__(self, nomi):
        self.subname = nomi
        self.numOfStuds = 0
        self.studs = []
    
    def add_student(self, student):
        """Subjectga student qo'shuvchi metod"""
        self.numOfStuds += 1
        self.studs.append(student)
    
    def get_name(self):
        """Subject name"""
        return self.subname

    def get_students(self):
        """Subjectga yozilgan studentlar haqida malumotni qaytaruvchi metod"""
        return [x.get_info() for x in self.studs]
    
    def get_studs_num(self):
        """Subjectga yozilgan studentlar sonini qaytaruvchi metod"""
        return self.numOfStuds
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is not True]
    
student1 = Student("Alex", "Bold", 1998)
math = Subject("Advanced Math")
math.add_student(student1)
math_studs = math.get_students()

print(see_methods(Student))
print(see_methods(Subject))
print(student1.__dict__)
print(student1.__dict__.keys())
print(student1.__dict__.values())





    