import pytest

from problem_5.main import brackets_are_valid


@pytest.mark.parametrize(
    'string, expected', [
        ('((()))', True),
        ('[()]{}', True),
        ('({[)]', False),
        ('', True)
    ]
)
def test_solution(string: str, expected: bool):
    result = brackets_are_valid(string)
    assert result == expected
