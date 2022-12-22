class Student:
    def __init__(self,name):
        self.name = name



class Teacher(Student):
    def __init__(self,age):
        self.age = age


class Run(Teacher):
    def __init__(self,name):
        self.name = name
    def run(self):
        print(self.name,'is runing')

# r = Run('Nurlan')
# r.run()


class Fly(Run):
    def __init__(self,age):
        self.age=age
    def fly(self):
        print('age is',self.age,)
# f = Fly(20)
# f.fly()

class Last(Fly):
    def __init__(self,name,age):
        self.name=name
        self.age=age
r = Run('Nurlan')
r.run()

f = Fly(20)
f.fly()


# class President(Student,Teacher,Run,Fly):...
#
# press = President('Sadyr',55)
# press.run()
#     def __str__(self):
#         return f'name is {self.name}\n'\
#                f'age is {self.age}\n'\
#                f'{self.name} is running\n'\
#                f'{self.name} is flying'
# pres = President("Sadyr",50)
# print(pres.name,pres.age,pres.run(),pres.fly())
