"""Thanks to Nikhil Kumar at https://www.geeksforgeeks.org/timeit-python-examples/ for a concise walkthrough
of timeit"""

import timeit

def is_unique_without_dictionary(a_string:str):
    """Return True if a string has all unique characters, False if there are repeats.

    """
    # #if length of character set is known, can do a fail-fast check against that
    # #i.e. if ASCII, then:
    #
    # if len(a_string) > 256:
    #     return False

    # no additional data structures AND if can use sorting


    a_string = sorted(a_string)

    for i in range(0, (len(a_string) - 1)):
        if a_string[i] == a_string[i + 1]:
            return False

    return True


def is_unique_with_dictionary(a_string:str):
    """Return True if a string has all unique characters, False if there are repeats.
    """
    # #if length of character set is known, can do a fail-fast check against that
    # #i.e. if ASCII, then:
    #
    # if len(a_string) > 256:
    #     return False

    characters = {}

    for char in a_string:
        if characters.get(char):
            return False
        else:
            characters[char] = True

    return True

def is_unique_no_sorting(a_string:str):
    """Return True if a string has all unique characters, False if there are repeats.

    """
    # #if length of character set is known, can do a fail-fast check against that
    # #i.e. if ASCII, then:
    #
    # if len(a_string) > 256:
    #     return False

    #

    for i in range(0, len(a_string)):
        if a_string[i] in a_string[(i + 1):]:
            return False

    return True


def time_is_unique_with_dictionary():
    SETUP_CODE = '''
from __main__ import is_unique_with_dictionary
from string import printable'''

    TEST_CODE = '''
test_string = printable
is_unique_with_dictionary(test_string)'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=5,
                          number=10000)

    print('Using a dictionary to find out if a string has all unique characters - min time: {}'.format(min(times)))
    print('Using a dictionary to find out if a string has all unique characters - max time: {}'.format(max(times)))


def time_is_unique_no_sorting_only_strings():
    SETUP_CODE = '''
from __main__ import is_unique_no_sorting
from string import printable'''

    TEST_CODE = '''
test_string = printable
is_unique_no_sorting(test_string)'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=5,
                          number=10000)

    print('Using no additional data structures and no sorting to find out if a string has all unique characters -  min time: {}'.format(
        min(times)))
    print(
        'Using no additional data structures and no sorting to find out if a string has all unique characters -  max time: {}'.format(
            max(times)))


def time_is_unique_with_sorting_only_strings():
    SETUP_CODE = '''
from __main__ import is_unique_without_dictionary
from string import printable'''

    TEST_CODE = '''
test_string = printable
is_unique_without_dictionary(test_string)'''

    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=5,
                          number=10000)

    print('Using no additional data structures to find out if a string has all unique characters - min time: {}'.format(
        min(times)))
    print('Using no additional data structures to find out if a string has all unique characters - max time: {}'.format(
        max(times)))



if __name__ == "__main__":
    time_is_unique_with_dictionary()
    time_is_unique_with_sorting_only_strings()
    time_is_unique_no_sorting_only_strings()


