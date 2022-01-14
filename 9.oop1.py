class Student:
    """Student nomli klass yaratamiz"""
    def __init__(self, ism, familya, tyil):
        self.name = ism
        self.surname = familya
        self.year = tyil
        self.grade = 1
    def get_fullname(self):
        return f"{self.name} {self.surname}"
    def get_info(self):
        return f"{self.name} {self.surname}, {self.grade}-grade student"
    def get_year(self, curYear):
        return f"{curYear - self.year}"
    def set_grade(self, bosqich):
        self.grade = bosqich
    def update_grade(self):
        self.grade += 1    

student1 = Student("Alex", "Bold", 1998)
student2 = Student("Alijon", "Valiyev", 2000)
student3 = Student("Hasan", "Alimov", 2001)
print(student3.get_info())

print(f"My name is {student1.get_fullname()}.")
print(f"I'm {student1.get_year(2022)} years old.")
print(f"I'm a {student1.grade}-year student.")

class Subject:
    """Subject nomli class yaratamiz"""
    def __init__(self, subName):
        self.name = subName
        self.numOfStuds = 0
        self.students = []
    def add_student(self, student):
        """Subject ga talabalar qo'shish"""
        self.numOfStuds += 1
        self.students.append(student)
    def get_student(self):
        return [student.get_info() for student in self.students]
math = Subject("Advanced Maths")
math.add_student(student1)
math.add_student(student2)
math.add_student(student3)

math_students = math.get_student()

print(math.numOfStuds)
print(math_students)





