def maxSubArray(nums) -> int:
    """
    Find the largest possible sum of any contiguous subarray.

    >>> maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) #[4,-1,2,1] has sum of 6
    6

    >>> maxSubArray([-2, -1, -2, -2])
    -1

    """
        
    #initalize a best sum and a current best sum to first item in array
    best = current_max = nums[0]
  
    #loop over rest of array
    for i in range(1,len(nums)):
        #compare the current element to the sum of the current best sum and the current element
        current_max = max(nums[i], current_max + nums[i])
        #compare best sum and current sum
        best = max(best, current_max) 
    
    #after all comparisons made, return highest possible sum
    return best
        

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
        