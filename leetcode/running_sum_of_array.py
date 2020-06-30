

def find_running_sum(nums: list) -> list:
    """Return an array of the running sum of a given input array

    >>> find_running_sum([1, 1, 1, 1])
    [1, 2, 3, 4]

    >>> find_running_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    """

    return [sum(nums[:idx+1]) for idx in range(len(nums))]


assert find_running_sum([1, 1, 1, 1]) == [1, 2, 3, 4]
assert find_running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]