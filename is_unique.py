"""Does a string have all unique characters?"""

def is_unique(phrase:str):
    """Determine if all characters in a string are unique."""
    
    #Solution 1 - O(n)
    return len(phrase) == len(set(phrase))

    #Solution 2 - O(n²)
    # for idx, char in enumerate(phrase):
    #     if char in phrase[idx + 1:]:
    #         return False
    # return True


assert is_unique("abaaaa") == False
assert is_unique("abcdefghijklmnopqrstuvwxyz") == True


"""Topics to study: Unicode/ASCII"""