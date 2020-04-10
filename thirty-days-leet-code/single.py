def singleNumber(nums) -> int:
    """Find the only num that isn't repeated.
    >>> singleNumber([4, 1, 1, 1])
    4
    """

    nums_ocurr = {}

    for num in nums:
        nums_ocurr[num] = nums_ocurr.get(num, 0) + 1

    for key, value in nums_ocurr.items():
        if value == 1:
            single = key

    return single
    

if __name__ == "__main__":
        import doctest
        if doctest.testmod().failed == 0:
            print("\n*** ALL TESTS PASSED. YAY!\n")