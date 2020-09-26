# This problem was recently asked by Google:
#
# Given a singly-linked list, reverse the list. This can be done iteratively or recursively.
# Can you get both solutions?
#
# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x: int):
        self.val = x
        self.next = None

    def __eq__(self, other):
        while self.next is not None:
            if self.val != other.val:
                return False
            return self.next.__eq__(other.next)

        return True


def reverse_singly_linked_list_iteratively(head: ListNode) -> ListNode:
    """Solution in O(n) time, O(1) space."""

    previous = None

    while head is not None:
        following = head.next
        head.next = previous
        previous = head
        head = following

    return previous


def reverse_singly_linked_list_recursively(head: ListNode) -> ListNode:
    """Solution in O(n) time, O(n) space."""

    if head.next is None:
        return head

    rest = reverse_singly_linked_list_recursively(head.next)

    head.next.next = head
    head.next = None

    return rest
