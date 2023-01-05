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

    def binary_search(lst, search_item):
        low = 0
        high = len(lst) - 1
        search_res = None

        while low <= high and not search_res:
            middle = (low + high) // 2
            guess = lst[middle]
            if guess == search_item:
                search_res = guess
            if guess > search_item:
                high = middle - 1
            else:
                low = middle + 1
        return search_res

    value = 68
    result = binary_search(get_list(), value)
    if result:
        print("Элемент найден!",result)
    else:
        print("Элемент не найден.",result)




