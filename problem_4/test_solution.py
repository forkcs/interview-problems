import pytest
from typing import List, Tuple

from problem_4.main import find_first_and_last_indicies


@pytest.mark.parametrize(
    'lst, target, expected', [
        ([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9, (6, 8)),
        ([100, 150, 150, 153], 150, (1, 2)),
        ([1, 2, 3, 4, 5, 6, 10], 9, (-1, -1))
    ]
)
def test_solution(lst: List[int], target: int, expected: Tuple[int, int]):
    result = find_first_and_last_indicies(lst, target)
    assert result == expected
