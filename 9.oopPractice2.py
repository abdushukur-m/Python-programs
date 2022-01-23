import math
import re


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

    def __repr__(self):
        return f"{self.ism} {self.familiya} {self.passport} {self.tyil}-yilda tug'ilgan"

#print(inson1)

#print(inson1 > inson2)
#print(inson1 >= inson2)
#print(inson1 < inson2)
#print(inson1 <= inson2)
#print(inson1 == inson2)
#print(inson1 != inson2)

class Student(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, bosqich):
        super().__init__(ism, familiya, passport, tyil)
        self.bosqich = bosqich
    
    def get_info(self):
        return f"{self.ism} {self.familiya}"


student1 = Student("Abdushukur", "Mukhiddinov", "AA0123456", 1998, 2)
student2 = Student("Alex", "Bold", "AB1234567", 1999, 1)

#print(student2)

class Fan:
    def __init__(self, fannomi):
        self.fannomi = fannomi
        self.numOfStuds = 0
        self.students = []

    def add_student(self, *studs):
        for student in studs:
            if isinstance(student, Student):
                self.students.append(student)
    
    def get_fan_info(self):
        return [student.get_info() for student in self.students]
   
    def __lt__(self, other):
        return self.tyil < other.tyil
    
    def __le__(self, other):
        return self.tyil < other.tyil

    def __eq__(self, other):
        return self.tyil == other.tyil

    def __getitem__(self, index):
        return self.students[index]

    def __setitem__(self, index, value):
        if isinstance(value, Student):
            self.students[index]=value

    def __len__(self):
        return len(self.students)

    def __add__(self, other):
        if isinstance(other, Fan):
            jami = Fan("{} + {}".format(self.fannomi, other.fannomi))
            jami.students = self.students + other.students
            return jami

    def __call__(self):
        return [stud for stud in self.students]

maths = Fan("Maths")
english = Fan("English")

student3 = Student("Tom", "Hanks", "AA4567891", 2002, 3)
student4 = Student("Bob", "Hardy", "AA9873210", 2003, 1)

maths.add_student(student1, student2)
english.add_student(student3, student4)

#maths[0]=student3
#print(len(maths))

print(maths())
print(english())
total = maths + english
print(total())