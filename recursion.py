"""Recursion practice"""

#helper classes

class Node(): #nodes for LLs
    def __init__(self, data, next = None):
        self.data = data
        self.next = next




def range_sum(begin, end, step):
    """
    Return the sum of a range of integers.  The range is defined by 3
    non-negative values: begin, end, step.  If begin is greater than end,
    return 0.

    >>> range_sum(2, 2, 2)
    2

    >>> range_sum(2, 6, 2) # 2 + 4 + 6 = 13
    12

    >>> range_sum(1, 5, 1) # 1 + 2 + 3 + 4 + 5 = 15
    15

    >>> range_sum(1, 5, 3) # 1 + 4 = 5
    5

    """
    if end - begin < 0:
        return 0

    return begin + range_sum(begin + step, end, step)

def sum_nested(lst):
    """
    >>> sum_nested([1, [2, [3, 5], 5], 6])
    22

    >>> sum_nested([1, 1, 1, [1, 1], 1])
    6
        
    """
    output = 0
    for item in lst:
        output += item if not isinstance(item, list) else sum_nested(item)

    return output

def stringify(node):
    """ 
    Uses prebuilt Node class. Create a function which accepts an argument of a 
    linked list and returns a string representation of the list.  The string
    representation 

    >>> stringify(Node(1, Node(2, Node(3))))
    '1 -> 2 -> 3 -> None'

    >>> stringify(None)
    'None'

    """
    output = ""
    if not node:
        return output + "None"
    return output + str(node.data) + " -> " + stringify(node.next)

    # if not node:
    #     return 'None'
    # return f'{node.data} -> {stringify(node.next)}'


def find_max(lst):
    """Find the max in a list of integers recursively


    >>> find_max([1, 2, 3, 97])
    97

    >>> find_max([1, 1, 1, 1])
    1

    # >>> find_max([])
    # 0

    >>> find_max([97, 5, 4])
    97

    >>> find_max([3, 2, -98])
    3

    >>> find_max([3, 100, 1])
    100


    """
    if len(lst) == 1:
        return lst[0]
    else:
        highest = find_max(lst[1:])
        if lst[0] > highest:
            return lst[0]
        else:
            return highest

def print_list(lst):
    """Prints out each element in a list recursively.

    >>> print_list(["apple", "berry", "cherry"])
    apple
    berry
    cherry

    >>> print_list([1, 2, 3])
    1
    2
    3

    """
    if len(lst) == 1:
        print(lst[0])
    else:
        print(lst[0])
        return print_list(lst[1:])




"""
Write a function that takes a list of integers, and finds the maximum of the list using recursion.
Write a function that prints out each element in a given list using recursion.
Write a function that prints out the integers 1 through 5 using recursion.
Write a function that takes a list of integers, and returns a list of each integer in that list doubled, using recursion."""


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")

