from functools import reduce
import operator


def does_sum(lst, n):
    """Return whether any two numbers in a given list sum to a given num

    >>> does_sum([10, 15, 3, 7], 17)
    True

    >>> does_sum([10, 11, 12], 100)
    False

    """

    for num in lst:
        if (n - num) in set(lst):
            return True
    return False

def prod(lst):
    """
    >>> prod([1, 2, 3])
    6

    >>> prod([2, 3, 4])
    24
    """
    
    return reduce(operator.mul, lst, 1)

def get_product_less_idx_element(lst):
    """Return an array with each element at index i is the product of all the numbers
    except the one at i in a given array

    >>> get_product_less_idx_element([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]

    >>> get_product_less_idx_element([3, 2, 1])
    [2, 3, 6]
    """

    return [int(prod(lst)/num) for num in lst]

def find_matching_paren(phrase, position):
    """Returns the index of the matching closing paren for a given opening
    >>> find_matching_paren("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)
    79

    >>> find_matching_paren("Help, (I'm trapped!))", 6)
    19
    """

    open_parens = 0
    for idx, char in enumerate(phrase):
        if char == "(":
            open_parens += 1
        if char == ")":
            open_parens -= 1
            if open_parens == 0:
                return idx

    raise Exception("No closing parens")


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")