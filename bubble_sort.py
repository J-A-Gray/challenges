import random

def bubble_sort(lst:list) -> list:
    """Optimized bubble sort

    >>> bubble_sort([1, 3, 2, 2, 0])
    [0, 1, 2, 2, 3]

    >>> random_nums = random.sample(range(-10000, 10000), 1000)
    >>> bubble_sort(random_nums) == sorted(random_nums)
    True

    """
    #loop over every item in list, except lat element
    for i in range(len(lst) - 1):
        #keep track if any swaps happen
        made_swap = False
        #compare current element to all other elements in the list, excluding
        #elements already sorted
        for j in range(len(lst) - 1 - i):
            #if current element is larget than next element, swap their places
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # and keep track that a swap happened
                made_swap = True
        #if no swaps happened, list is already sorted
        if not made_swap:
            break
    
    return lst