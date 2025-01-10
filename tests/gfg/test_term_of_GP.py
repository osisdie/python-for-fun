import math

import pytest


# a*b^(n-1)
def term_of_GP(a: int, b: int, n: int) -> int:
    if n == 1:
        return a

    res = a
    r = b / a # common ratio
    for _ in range(n-1): #1->0
        res *= r
    return math.floor(res)

# O(logN)
def term_of_GP_optimized(a: int, b: int, n: int) -> int:
    if n == 1:
        return a

    def power(x: float, y: int) -> float:
        result = 1
        while y > 0:
            if y%2 == 1: # if y is odd, multiply result by x
                result *= x
            x *= x
            y //= 2
        return result

    r = b / a # common ratio
    term = a * power(r, n - 1)
    return math.floor(term)


@pytest.mark.parametrize(
    ("a", "b", "n", "expected"),
    (
        (2, 3, 1, 2),
        (1, 2, 5, 16),
        (84, 87, 3, 90),
        (87, 93, 5, 113),
    ),
)
def test_term_of_GP(
    a: int, b: int, n: int,
    expected: int
) -> None:
    assert expected == term_of_GP(a,b,n)
    assert expected == term_of_GP_optimized(a,b,n)
