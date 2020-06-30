
def shuffle_array(nums:list, n:int) -> list:
    """Return an array in the format [x1, y1, x2, y2,...,xn, yn] given an array
    in format [x1, x2, ..., xn, y1, y2, ..., yn]
    
    >>> shuffle_array(nums = [2, 5, 1, 3, 4, 7], n = 3)
    [2, 3, 5, 4, 1, 7]

    >>> shuffle_array(nums = [1, 2, 3, 4, 4, 3, 2, 1], n = 4)
    [1, 4, 2, 3, 3, 2, 4, 1]

    >>> shuffle_array(nums = [1, 1, 2, 2], n = 2)
    [1, 2, 1, 2]

    """
    
    results = []

    for i in range(n):
        results.append(nums[i])
        results.append(nums[i + n])

    return results

    

assert shuffle_array(nums = [2,5,1,3,4,7], n = 3) == [2, 3, 5, 4, 1, 7]
assert shuffle_array(nums= [1,2,3,4,4,3,2,1], n = 4) == [1, 4, 2, 3, 3, 2, 4, 1]
assert shuffle_array(nums = [1, 1, 2, 2], n = 2) == [1, 2, 1, 2]
