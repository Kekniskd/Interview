# Problem #1 (Easy): String manipulation
# Write a Python function, is_anagram, that takes two strings as input and determines whether they are anagrams of each other. Anagrams are words or phrases that use the same set of characters in a different order.
# Input: "listen", "silent"
# Output: True
# Input: "hello", "world"
# Output: False


def check_anagram(str1: str, str2: str) -> bool:
    str1_dict = {}
    str2_dict = {}
    for letter in str1:
        str1_dict[letter] = str1_dict.get(letter, 0) + 1
    for letter in str2:
        str2_dict[letter] = str2_dict.get(letter, 0) + 1
    for letter in str1_dict.keys():
        if letter in str1_dict and letter in str2_dict:
            if str1_dict[letter] != str2_dict[letter]:
                return False
        else:
            return False

    return True


check_anagram("hello", "world")


# Problem #2: List, For Loops
# Create a function, find_highest, that accepts a list of integers and returns the list whose sum of elements is the highest.
# For example:
# Input: [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# Output: [10, 11, 12]

def max_list(li: list) -> list:
    max_sum = 0
    max_sum_list = None

    for item in li:
        curr_sum = sum(item)
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_sum_list = item
    return max_sum_list


max_list([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]])

import pandas as pd

df = pd.DataFrame({'year': [2013, 2010, 2013, 2011, 2012, 2012, 2010, 2011],

                   'issuer': ['A', 'B', 'B', 'B', 'A', 'B', 'A', 'A'],

                   'emissions': ['325', 301, 201, 111, 901, '212', 255, None]

                   })
