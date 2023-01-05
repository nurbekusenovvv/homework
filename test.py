def get_list() -> list:
    return list(range(0, 1_000_000, 2))

def get_target():
    return 4
"""
    what is Binary Search?
    then do Solution for search target in list
"""


class Solution():
    """
        find_target -> YOUR_CODE
    """


    def find_target(self, list, target):
        for k in enumerate(list):
            if k[1] == target:
                return k[0]
        return None


print('искомый элемент',get_target(),'находится под индексом',Solution())



