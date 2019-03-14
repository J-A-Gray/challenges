

def does_sum(lst, n):
    """Returns whether any two numbers in a given list sum to a given num

    >>> does_sum([10, 15, 3, 7], 17)
    True

    >>> does_sum([10, 11, 12], 100)
    False

    """

    for num in lst:
        if (n - num) in set(lst):
            return True
    return False





if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")