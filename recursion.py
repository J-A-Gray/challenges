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
    # output = 0
    # for item in lst:
    #     output += item if not isinstance(item, list) else sum_nested(item)

    # return output

    if len(lst) == 0:
        return 0
    else:
        head = lst[0]
        if isinstance(head, int):
            return head + sum_nested(lst[1:])
        else:
            return sum_nested(head) + sum_nested(lst[1:])


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


def print_integers(n):
    """Write a function that prints out the integers 1 through n using recursion
    
    >>> print_integers(5)
    1
    2
    3
    4
    5

    >>> print_integers(2)
    1
    2

    """
    if n >= 1:
        print_integers(n-1)
        print(n)


def double_list(lst):
    """Return a list of given integers doubled

    >>> double_list([1, 2, 3])
    [2, 4, 6]

    >>> double_list([2, 2, 2])
    [4, 4, 4]

    """
    # new_lst = []
    # for n in lst:
    #     if isinstance(n, list):
    #         print_doubled_integers(n)
    #     else:
    #         new_lst.append(n*2)
    # return new_lst

    #no iteration version
    if len(lst) == 0:
        return []
    else:
        return[lst[0]*2] + double_list(lst[1:])

def get_factorial(n):
    """Return the factorial of a given integer

    >>> get_factorial(6)
    720

    >>> get_factorial(4)
    24

    """

    if n == 1:
        return n

    return n * get_factorial(n-1)

def get_even(lst):
    """Return a list of even integers, given a list of integers

    >>> get_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]

    >>> get_even([2, 2, 2])
    [2, 2, 2])

    >>> get_even([])
    []

    """
    if len(lst) == 0:
        return []
    else:
        if lst[0] % 2 == 0:
            return lst[0] + get_even(lst[1:])
        else:
            return get_even(lst[1:])

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")

