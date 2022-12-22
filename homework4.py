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



