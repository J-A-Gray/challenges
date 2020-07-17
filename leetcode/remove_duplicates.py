def remove_duplicates(nums:list) -> int:
    """Without changing size of original array and via manipulating it in place, 
    return the integer that represents the end of a subsection with only unique 
    elements. Constant space, two pointer problem.

    >>> nums = [1, 2, 2, 3, 4, 4, 5, 6]
    >>> unique_len = remove_duplicates(nums)
    >>> unique_len == 6
    True
    >>> nums[:unique_len] == [1, 2, 3, 4, 5, 6]
    True


    >>> nums = [1, 1, 1, 1]
    >>> unique_len = remove_duplicates(nums)
    >>> unique_len == 1
    True

    >>> nums[:unique_len] == [1]
    True
    """

    if len(nums) == 0:
        return 0

    #track end of unique section of array
    i = 0
    #increment over the array, j is current index
    for j in range(len(nums)):
        #if current element is not the same as element 
        #at the end of unique subsection,
        #increase the subsection endpoint variable and move unique element there
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1
