import collections
import re

# using slicing
def valid_palindrome_using_slicing(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


s = input()
valid_palindrome_using_slicing(s)

# standard version
# def valid_palindrome(s: str) -> bool:
#     strs = []
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.pop(0) != strs.pop():
#             return False
#
#     return True

# using Deque
# def valid_palindrome_using_deque(s: str) -> bool:
#     strs = collections.deque()
#     for char in s:
#         if char.isalnum():
#             strs.append(char.lower())
#
#     while len(strs) > 1:
#         if strs.popleft() != strs.pop():
#             return False
#
#     return True
#
#

