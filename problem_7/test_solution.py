import pytest
from typing import List

from problem_7.main import two_sum


@pytest.mark.parametrize(
    'lst, k, expected', [
        ([4, 7, 1, -3, 2], 5, True),
        ([4, 7, -1, -3, 10], 5, False),
        ([1, 0], 1, True),
        ([1], 1, False),
        ([-1, -1], 2, False)
    ]
)
def test_solution(lst: List[int], k: int, expected: bool):
    assert two_sum(lst, k) == expected
