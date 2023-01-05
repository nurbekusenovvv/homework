def get_list() -> list:
    return list(range(0, 1_000_000, 2))

# def get_target():
#     return 4





"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution():
    """
        find_target -> YOUR_CODE
    """
    nu = 44

    lowest = 0
    highest = len(get_list()) - 1
    index = None

    while (lowest <= highest) and (index is None):
        # повторять пока не найдем
        mid = (lowest + highest) // 2
        if get_list()[mid] == nu:
            index = mid
        else:
            if nu < get_list()[mid]:
                # ищем по левой части списка
                highest = mid - 1
            else:
                # по правой
                lowest = mid + 1

    print('искомый элемент', nu, 'находиться под индексом', index)

