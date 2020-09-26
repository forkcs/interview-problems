import pytest
from typing import Callable, List

from problem_1.main import ListNode, add_two_numbers


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


@pytest.mark.parametrize(
    'list1, list2, expected_result',
    (
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([1, 9, 9], [3, 4, 5], [4, 3, 5, 1]),
        ([9, 9, 9], [9, 9, 9], [8, 9, 9, 1])
    )
)
def test_solution(list1: List[int], list2: List[int], expected_result: List[int], create_linked_list):
    l1 = create_linked_list(list1)
    l2 = create_linked_list(list2)

    solution = add_two_numbers(l1, l2)
    expected = create_linked_list(expected_result)
    assert solution == expected
