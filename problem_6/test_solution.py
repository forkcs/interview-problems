import pytest
from typing import Callable, List

from problem_6.main import ListNode, reverse_singly_linked_list_iteratively, reverse_singly_linked_list_recursively


@pytest.fixture
def create_linked_list() -> Callable:
    def make_linked_list(lst: List[int]) -> ListNode:
        result = []
        prev_el = None
        for el in lst:
            new_el = ListNode(el)
            if prev_el is not None:
                prev_el.next = new_el
            else:
                result = new_el
            prev_el = new_el
        return result
    return make_linked_list


test_lists = (
    ([0, 1, 2, 3, 4], [4, 3, 2, 1, 0]),
    ([0, 1], [1, 0]),
    ([0], [0])
)


@pytest.mark.parametrize(
    'lst, expected', test_lists
)
def test_iterative_solution(lst: List[int], expected: List[int], create_linked_list):
    linked_list = create_linked_list(lst)
    expected_linked_list = create_linked_list(expected)
    reversed_linked_list = reverse_singly_linked_list_iteratively(linked_list)
    assert reversed_linked_list == expected_linked_list


@pytest.mark.parametrize(
    'lst, expected', test_lists
)
def test_recursive_solution(lst: List[int], expected: List[int], create_linked_list):
    linked_list = create_linked_list(lst)
    expected_linked_list = create_linked_list(expected)
    reversed_linked_list = reverse_singly_linked_list_recursively(linked_list)
    assert reversed_linked_list == expected_linked_list
