import math

import pytest


def is_prime(N: int) -> bool:
    if N == 1:
        return False
    if N in (2, 3):
        return True
    if N%2 ==0 or N%3==0:
        return False

    for i in range(5, math.ceil(math.sqrt(N)) + 1, 6):
        if (N%i == 0) or (N%(i+2) == 0):
            return False
    return True

@pytest.mark.parametrize(
    ("N", "expected"),
    (
        (5, True),
        (4, False),
    ),
)
def test_test_factorial(
    N: int,
    expected: bool
) -> None:
    assert expected == is_prime(N)
