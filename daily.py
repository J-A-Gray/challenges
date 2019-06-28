from functools import reduce
import operator
from typing import List, Any, Tuple, Union


def does_sum(lst, n):
    """Return whether any two numbers in a given list sum to a given num

    >>> does_sum([10, 15, 3, 7], 17)
    True

    >>> does_sum([10, 11, 12], 100)
    False

    """

    for num in lst:
        if (n - num) in set(lst):
            return True
    return False

def prod(lst):
    """
    >>> prod([1, 2, 3])
    6

    >>> prod([2, 3, 4])
    24
    """
    
    return reduce(operator.mul, lst, 1)

def get_product_less_idx_element(lst):
    """Return an array with each element at index i is the product of all the numbers
    except the one at i in a given array

    >>> get_product_less_idx_element([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]

    >>> get_product_less_idx_element([3, 2, 1])
    [2, 3, 6]
    """

    return [int(prod(lst)/num) for num in lst]


def find_matching_paren(phrase, position):
    """Returns the index of the matching closing paren for a given opening
    >>> find_matching_paren("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)
    79

    >>> find_matching_paren("Help, (I'm trapped!))", 6)
    19
    """

    open_parens = 0
    for idx, char in enumerate(phrase):
        if char == "(":
            open_parens += 1
        if char == ")":
            open_parens -= 1
            if open_parens == 0:
                return idx

    raise Exception("No closing parens")



def find_anagrams_by_indices(word, S):

    """Given a word and a string S, find all starting indices in S which are anagrams of word.

    For example, given that word is “ab”, and S is “abxaba”, return 0, 3, and 4.

    >>> find_anagrams_by_indices("ab", "abxaba")
    [0, 3, 4]

    >>> find_anagrams_by_indices("cat", "zzzzzzzzz")
    []

    >>> find_anagrams_by_indices("aba", "bab")
    []

    """
    indices = []
    slice_start = 0
    slice_end = slice_start + len(word)


    while slice_end <= len(S):
        if sorted(word) == sorted(S[slice_start:slice_end]):
            indices.append(slice_start)

        slice_end += 1
        slice_start += 1


    return indices

def find_unique_integer(id_list):
    """Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.
    >>> find_unique_integer([1, 2, 2, 3, 3, 5, 6, 7, 7, 8, 5, 8, 6])
    1

    :param id_list
    :type id_list: list
    :rtype: int

    """
    ids = set()
    for num in id_list:
        if not num in ids:
            ids.add(num)
        else:
            ids.remove(num)

    return ids.pop()

def reverse_only_alpha_chars(phrase:str):
    """Reverse only the letters in a string, leaving the numbers as-is.
    >>> reverse_only_alpha_chars('abc23xz')
    'zxc23ba'

    >>> reverse_only_alpha_chars('a')
    'a'

    >>> reverse_only_alpha_chars('')
    ''

    >>> reverse_only_alpha_chars('123456')
    '123456'

    >>> reverse_only_alpha_chars('1a2b3c')
    '1c2b3a'

    :type phrase: str
    :rtype: str

    """

    if len(phrase) <= 1 or phrase.isdigit(): #win quick
        results = phrase

    else:
        results = ""

        letters = [char for char in phrase if char.isalpha()] #python list as a stack


        for char in phrase:
            if char.isalpha():
                results += letters.pop() #will pop off in lifo order

            else:
                results += char


    return results



def toggle_hats(num_cats:int):
    """
    You have n number of cats, none of which are wearing hats.  Every time you interact with a cat, they will either
    put on  a hat if they aren't wearing a hat or take off the hat they are wearing.  You will interact with the
    group of cats n times (as many times as they are cats).  The first time you will interact with every cat, the
    second time every other cat, the third time every third cat, etc.  Return an array of the state of each cat at the
    end of n rounds of interaction.  If the cat is wearing a hat, they will be represented by the bool True, if they
    are not wearing a hat, they will be represented by the bool False.

    >>> toggle_hats(16)
    [True, False, False, True, False, False, False, False, True, False, False, False, False, False, False, True]


    :param num_cats
    :type num_cats: int
    :rtype: list

    """
    #create inital list of cats without hats - all elements False
    cats = []
    i = 0
    while i < num_cats:
        cats.append(False)
        i += 1
    # print("Before toggling, cats is")
    # print(cats)

    #begin toggling rounds
    toggle = 1
    while toggle <= num_cats:
        # print("Round is", toggle)
        for idx, cat in enumerate(cats):
            # print(idx + 1, cat)
            if (idx + 1) % toggle == 0:
                cats[idx] = not(cat)

        toggle += 1

    return cats

#1.1 from CtCI
def is_unique(a_string:str):
    """Return True if a string has all unique characters, False if there are repeats.

    >>> is_unique("abcdefg")
    True

    >>> is_unique("AaBbCc")
    True

    >>> is_unique("aa")
    False

    >>> is_unique("1234567891")
    False
    """
    # #if length of character set is known, can do a fail-fast check against that
    # #i.e. if ASCII, then:
    #
    # if len(a_string) > 256:
    #     return False

    #

    # # no additional data structures AND if can use sorting
    #
    a_string = sorted(a_string)

    for i in range(0, (len(a_string) - 1)):
        if a_string[i] == a_string[i + 1]:
            return False

    return True


    #only strings, no sorting
    #
    # for i in range(0, len(a_string)):
    #     if a_string[i] in a_string[(i + 1):]:
    #         return False
    #
    # return True

    # #dict solution
    # characters = {}
    #
    # for char in a_string:
    #     if characters.get(char):
    #         return False
    #     else:
    #         characters[char] = True
    #
    # return True


#1.3 from CtCI

def replace_space_characters(phrase:list):
    """Replace all single spaces with %20 in a list (done in list in order to manipulate the data structure in place)

    >>> replace_space_characters(list('Jane Developer'))
    ['J', 'a', 'n', 'e', '%', '2', '0', 'D', 'e', 'v', 'e', 'l', 'o', 'p', 'e', 'r']

    >>> test_phrase = "Sarah Engineer"
    >>> test_phrase = list(test_phrase)
    >>> result = replace_space_characters(test_phrase)
    >>> result == ['S', 'a', 'r', 'a', 'h', '%', '2', '0', 'E', 'n', 'g', 'i', 'n', 'e', 'e', 'r']
    True
    >>> id(test_phrase) == id(result)
    True

    """

    for idx, char in enumerate(phrase):
        if phrase[idx] == " ":
            phrase[idx:idx+1] = ["%", "2", "0"]

    return phrase

def urlify(string, length):
    """Replace all single spaces with '%20' in a string.

    :param string:str
    :param length:int #length represents 'true' length of string with no trailing spaces
    :rtype str


    >>> test_length = len("what cannot be said will be wept")
    >>> urlify("what cannot be said will be wept            ", test_length)
    'what%20cannot%20be%20said%20will%20be%20wept'

    >>> urlify('Jane Developer  ', 14)
    'Jane%20Developer'

    """
    index = len(string) #length of string with trailing spaces, use to shift chars to make room
    str_list = list(string)

    for i in reversed(range(length)): #"true length" excludes trailing spaces, moving backwards through the chars
        if str_list[i] != " ":
            str_list[index - 1] = str_list[i]
            index -= 1

        else:
            str_list[index-3:index] = "%20"
            index -= 3 #skip three places toward the beginning


    return "".join(str_list)


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")


