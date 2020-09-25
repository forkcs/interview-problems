import pytest

from problem_3.main import sort_list, sort_list_in_constant_space


test_lists = [
    ([3, 3, 2, 1, 3, 2, 1], [1, 1, 2, 2, 3, 3, 3]),
    ([2, 3, 1], [1, 2, 3]),
    ([2, 2, 3, 3, 3, 1], [1, 2, 2, 3, 3, 3]),
    ([2, 2, 3, 3, 1, 1], [1, 1, 2, 2, 3, 3]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3])
]


@pytest.mark.parametrize('lst, expected', test_lists)
def test_solution(lst: list, expected: list):
    sorted_list = sort_list(lst)
    assert sorted_list == expected


@pytest.mark.parametrize('lst, expected', test_lists)
def test_constant_space_solution(lst: list, expected: list):
    sorted_list = sort_list_in_constant_space(lst)
    assert sorted_list == expected
