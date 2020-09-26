# This problem was recently asked by Google:
#
# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Example:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]


from typing import List


def sort_list_in_constant_space(lst: List[int]) -> List[int]:
    """Solution in O(n) time, O(1) space."""

    one_count = 0  # count of "1" elements
    i = 0  # index of current element
    three_count = len(lst) - 1  # count of "3" elements
    while i <= three_count:
        if lst[i] == 1:
            lst[one_count], lst[i] = lst[i], lst[one_count]
            one_count += 1
            i += 1
        elif lst[i] == 3:
            lst[three_count], lst[i] = lst[i], lst[three_count]
            three_count -= 1
        else:
            i += 1

    return lst
