import pytest

from problem_2.main import length_of_the_longest_substring


@pytest.mark.parametrize(
    's, expected', [
        ('abrkaabcdefghijjxxx', 10),
        ('abcde', 5),
        ('a', 1),
        ('aa', 1),
        ('aaa', 1),
        ('abcdee', 5),
        ('aabcde', 5)
    ]
)
def test_solution(s: str, expected: int):
    result = length_of_the_longest_substring(s)
    assert result == expected
