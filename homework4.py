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


class BirthYear(Run):
    def __init__(self,age):
        self.age=age
    def byear(self):
        print('year is', 2022-self.age)
# f = Fly(20)
# f.fly()

class Last(BirthYear):
    def __init__(self,name,age):
        self.name=name
        self.age=age
r = Run('Nurlan')
r.run()

bt= BirthYear(20)
bt.byear()



