def get_list() -> list:
    return list(range(0, 1_000_000, 2))


"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution:
    """
        find_target -> YOUR_CODE
    """

    def find_target(self, list, target):
        pass

name = [1,2,3,4,5,6,7,8,9]

search_for = 4  # что ищем


def linear_search(where, what):
    for k in enumerate(where):
        if k[1] == what:
            return k[0]  # возвращаем индекс

    return None


print('искомый элемент', search_for, 'найден под индексом',
      linear_search(name, search_for))