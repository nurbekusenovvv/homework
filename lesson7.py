# big(o)
# o(1)
# константа
# return -1
import random


g=range(1,10000)

print(sum(g))

# O(n)
# линейный прямо проц данных



g=range(1,10000)

# O(log n)
# бинарный


# o(n^2)
# квадратичная
# s=range(1,10000)
# h=range(1,10000)
#
# print(sum(s)+sum(h))
# 2 цикла


# o(n^3)



# O(n!)
# 5!=1*2*3*4*5
# все комбинации
##########################################


# линейный поиск

name = ['бека', 'beka', 'erf', 'нурислам', 'adahan']

search_for = 'нурислам'  # что ищем


def linear_search(where, what):
    for v in enumerate(where):
        if v[1] == what:
            return v[0]  # возвращаем индекс

    return None


print('искомый элемент', search_for, 'найден под индексом',
      linear_search(name, search_for))

# o(5)


# сортировка выборкой
# o(n2)

# сортировка выборкой
# o(n2)
nums = [2, 3, 1, 3, 1, 5, 7, 85, 5, 2, 2, 5, 6, 7, 0, 11, 33, 3, 44, 9, 9]

print('было', nums)

for i in range(len(nums)):
    lowest = i  # первый элемент за наименьший

    for j in range(i + 1, len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j

    nums[i], nums[lowest] = nums[lowest], nums[i]
n = 1
m = 2
n, m = m, n
print('стало', nums)

# o(log n)
# бинарный поиск

ma = sorted(nums)
print(ma)

nu = 0

lowest = 0
highest = len(ma) - 1
index = None

while (lowest <= highest) and (index is None):
    # повторять пока не найдем
    mid = (lowest + highest) // 2
    if ma[mid] == nu:
        index = mid
    else:
        if nu < ma[mid]:
            # ищем по левой части списка
            highest = mid - 1
        else:
            # по правой
            lowest = mid + 1

print('искомый элемент', nu, 'находиться под индексом', index)


# алгоритм Евклида - нахождение нод

def nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return b + a


print('НОД чисел 70 120=', nod(70, 120))

from math import gcd

print(gcd(70, 120))

# поворот строки

some_string = 'я не сегодня заболел!'


def reversee(s):
    chars = list(s)

    for i in range(len(s) // 2):
        #         до середины
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp

    return ''.join(chars)

print(some_string)
print(reversee(some_string))
# print(some_string[::-1])



