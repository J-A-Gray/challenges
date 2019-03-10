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
    pass

def sum_nested(lst):
    """
    >>> sum_nested([1, [2, [3, 5], 5], 6])
    22

    >>> sum_nested([1, 1, 1, [1, 1], 1])
    6
        
    """
    pass

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
    pass


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
    


def double_list(lst):
    """Return a list of given integers doubled

    >>> double_list([1, 2, 3])
    [2, 4, 6]

    >>> double_list([2, 2, 2])
    [4, 4, 4]

    """
    
    

def get_factorial(n):
    """Return the factorial of a given integer

    >>> get_factorial(6)
    720

    >>> get_factorial(4)
    24

    """
def get_even(lst):
    """Return a list of even integers, given a list of integers

    >>> get_even([1, 2, 3, 4, 5, 6])
    [2, 4, 6]

    >>> get_even([2, 2, 2])
    [2, 2, 2]

    >>> get_even([])
    []

    """
    
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")