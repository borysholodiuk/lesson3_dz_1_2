"""
Домашнє завдання
Потрібно створити клас Людина(Ім'я, Прізвище, Вік), який має заповнювати клас Студент.
Потрібно створити клас Студент(Людина(), стипендія(True / False)), який буде заповнювати клас Група.
Потрібно створити клас Група(назва групи, список студентів).
"""


class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"Name={self.name} Surname={self.surname} Age={self.age}"


class Student:
    def __init__(self, human: Human, stipend: bool):
        self.human = human
        self.stipend = stipend

    def __str__(self):
        return f"Student={self.human} Stipend={self.stipend}"


class Group:
    def __init__(self, name: str, students: list):
        self.name = name
        self.students = students

    def __str__(self):
        return f"GroupName={self.name}, Students={self.students}"

    def get_info(self):
        print(f"GroupName={self.name}")
        for student in self.students:
            print(student)


if __name__ == '__main__':
    andriy = Human(name="Andriy", surname="Gold", age=12)
    bober = Human(name="Bober", surname="Blodd", age=31)
    capibar = Human(name="Capibar", surname="Lobzik", age=5)

    student_andriy = Student(andriy, True)
    student_bober = Student(bober, False)
    student_capibar = Student(capibar, True)

    group = Group(name="Group1", students=[student_andriy, student_bober, student_capibar])
    group.get_info()
