# This problem was recently asked by AirBNB:
#
# Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a
# target element, x. Return -1 if the target is not found.
#
# Examples:
# Input: lst = [1,3,3,5,7,8,9,9,9,15], target = 9
# Output: (6, 8)
#
# Input: lst = [100, 150, 150, 153], target = 150
# Output: (1, 2)
#
# Input: lst = [1,2,3,4,5,6,10], target = 9
# Output: (-1, -1)


from typing import List, Tuple


def find_first_and_last_indicies(lst: List[int], target: int) -> Tuple[int, int]:
    """Solution in O(n) time, O(1) space."""

    first = -1
    last = -1
    for i in range(len(lst)):
        if lst[i] == target:
            if first == -1:
                first = i
            else:
                last = i

    return first, last
