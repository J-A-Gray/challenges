"""Is one string a permutation of another? Cracking the Coding Interview 1.2"""

def is_permutation(phrase1:str, phrase2:str):
    """Determines if one string is a permutation of another."""
    # Solution 1
    if len(phrase1) != len(phrase2):
        return False

    characters = {}

    for char in phrase1:
        characters[char] = characters.get(char, 0) + 1

    for char in phrase2:
        characters[char] = characters.get(char, 0) - 1
        
        if characters[char] == 0:
            del characters[char]

    return len(characters) == 0

    # Solution 2
    if len(phrase1) != len(phrase2):
        return False

    return sorted(phrase1) == sorted(phrase2)

assert is_permutation("moon", "noom") == True
assert is_permutation("moon", "cow") == False
assert is_permutation("moon", "noon") == False