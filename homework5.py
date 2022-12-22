from homework4 import Student
st = Student('Ferrari')
print(st)

from homework4 import Teacher
t = Teacher(21)
print(t)

from homework4 import Run
r = Run('Lamborgini')
r.run()

from homework4 import BirthYear
bt = BirthYear(21)
bt.byear()

from homework4 import Last
l = Last('Gitler',133)
l.run()
l.byear()




from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')