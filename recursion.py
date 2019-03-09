"""Recursion practice"""
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



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
