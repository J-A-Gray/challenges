def moveZeroes(nums) -> None:
        """
        Move all zeroes in an array to the end, without returning anything. 
        Modify input array in-place.

        >>> test1 = [4, 0, 0, 5, 8]
        >>> moveZeroes(test1)
        >>> test1 == [4, 5, 8, 0, 0]
        True

        
        >>> test_nums = [4, 0, 0, 5, 8]
        >>> nums_id = id(test_nums)
        >>> moveZeroes(test_nums)
        >>> id(test_nums) == nums_id
        True

        """
              
        nums[:] = [num for num in nums if num != 0] + ([0] * nums.count(0))

if __name__ == "__main__":
        import doctest
        if doctest.testmod().failed == 0:
            print("\n*** ALL TESTS PASSED. YAY!\n")