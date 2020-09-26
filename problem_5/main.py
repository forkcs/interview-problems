# This problem was recently asked by Uber:
#
# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses
# in the program are balanced. Every opening bracket must have a corresponding closing bracket.
# We can approximate this using strings.
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.
#
# Example:
# Input: "((()))"
# Output: True
#
# Input: "[()]{}"
# Output: True
#
# Input: "({[)]"
# Output: False

from collections import deque


def brackets_are_valid(string: str) -> bool:
    """Solution in O(n) time, O(n) space."""

    closing_brackets = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    opening = deque()  # parsed opening brackets
    for char in string:
        if char in closing_brackets.keys():
            opening.append(char)
        else:
            if not opening:
                return False
            if char != closing_brackets[opening.pop()]:
                return False
    return True
