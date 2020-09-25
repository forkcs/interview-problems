# This problem was recently asked by Microsoft:
#
# Given a string, find the length of the longest substring
# without repeating characters.
#
# Can you find a solution in linear time?
#
# Example:
# Input: abrkaabcdefghijjxxx
# Output: 10


def length_of_the_longest_substring(s: str) -> int:
    """Solution in O(n) time, O(1) space."""

    start = 0
    end = 1
    length = 1
    while end <= len(s):
        if s.count(s[end-1], start, end) == 1:
            new_length = end - start
            if new_length > length:
                length = new_length
            end += 1
        else:
            start += 1
    return length
