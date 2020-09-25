# This problem was recently asked by Microsoft:
#
# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain
# a single digit. Add the two numbers and return it as a linked list.
#
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2, c=0):
    """Solution in ?? time, ?? space."""

    while l1 is not None or c > 0:
        if l1 is not None:
            value = l1.val + l2.val + c
            if value > 9:
                c = 1
                value = value - 10
        else:
            value = c
            new_el = ListNode(value)
            return new_el

        new_el = ListNode(value)
        new_el.next = add_two_numbers(l1.next, l2.next, c=c)
        return new_el
