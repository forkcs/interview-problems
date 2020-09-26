import pytest
from typing import List

from problem_3.main import sort_list_in_constant_space


@pytest.mark.parametrize(
    'lst, expected', [
        ([3, 3, 2, 1, 3, 2, 1], [1, 1, 2, 2, 3, 3, 3]),
        ([2, 3, 1], [1, 2, 3]),
        ([2, 2, 3, 3, 3, 1], [1, 2, 2, 3, 3, 3]),
        ([2, 2, 3, 3, 1, 1], [1, 1, 2, 2, 3, 3]),
        ([1, 2, 3], [1, 2, 3]),
        ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3])
    ]
)
def test_constant_space_solution(lst: List[int], expected: List[int]):
    sorted_list = sort_list_in_constant_space(lst)
    assert sorted_list == expected
