class Student:

    graduating_year = 2026
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1


stu1 = Student("ashik", 22)
stu1 = Student("saif", 24)
stu1 = Student("Nahin", 25)

# print(stu1.name)
# print(stu1.age)
# print(Student.graduating_year)
print(Student.num_student)