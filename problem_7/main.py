# This problem was recently asked by Facebook:
#
# You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list
# that add up to k.
#
# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.
#
# Try to do it in a single pass of the list.


from typing import List


def two_sum(lst: List[int], k: int) -> bool:
    """Solution in O(n) time, O(n) space."""

    complements = set()
    for el in lst:
        if el in complements:
            return True
        complements.add(k - el)
    return False
