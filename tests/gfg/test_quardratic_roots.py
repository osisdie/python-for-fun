import math
from typing import Union

import pytest


# ax^2 + bx + c = 0
# D = b^2 - 4ac
def quardratic_roots(a: int, b: int, c: int) -> Union[list[int], list[str]]:
    D = b**2 - 4*a*c
    # (-b+D**0.5)/2a, (-b-D**0.5)/2a
    if D > 0:
        root1 = float(-b+math.sqrt(D))/(2*a)
        root2 = float(-b-math.sqrt(D))/(2*a)
        res = [math.floor(root1), math.floor(root2)]
        return [max(res), min(res)]
    elif D == 0:
        root = float(-b)/(2*a)
        return [math.floor(root), math.floor(root)]
    else:
        return ["Imaginary"]


@pytest.mark.parametrize(
    ("a", "b", "c", "expected"),
    (
        (1, -2, 1, [1, 1]),
        (1, -7, 12, [4, 3]),
        (752, 904, 164, [-1, -1]),
        (543, 199, 843, ["Imaginary"]),
        (-264, -750, 504, [0, -4]),
        (752, 904, 164, [-1, -1]),
    ),
)
def test_quardratic_roots(
    a: int, b: int, c: int,
    expected: list[int]
) -> None:
    assert expected == quardratic_roots(a,b,c)
