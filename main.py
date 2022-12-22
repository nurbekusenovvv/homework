class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return f'name is {self.name}'

student = Student('Nurbek')
print(student)

class Teacher:
    def __init__(self,age):
        self.age = age
    def __str__(self):
        return f'age is {self.age}'
teacher = Teacher(20)
print(teacher)

class Run:
    def run(self):
        print(self,'run')
#     def __str__(self):
#         return f'{self.name} is running'
# r = Run("Murat")
# print(r)

class Fly:
    def fly(self):
        print(self,'fly')
#     def __str__(self):
#         return f'{self.name} is flying'
# f = Fly("Nurlan")
# print(f)

class President(Student,Teacher,Run,Fly):...

press = President('Sadyr',55)
press.run()
#     def __str__(self):
#         return f'name is {self.name}\n'\
#                f'age is {self.age}\n'\
#                f'{self.name} is running\n'\
#                f'{self.name} is flying'
# pres = President("Sadyr",50)
# print(pres.name,pres.age,pres.run(),pres.fly())
