import math

import pytest


# Num of digits = logN! + 1
# logN! = log1 + log2 + .. logN
def digits_in_factorial(N: int) -> int:
    log_sum = 0
    for i in range(1, N+1): #1,2,3,4
        log_sum += math.log10(i)
    return int(log_sum) + 1


def digits_in_factorial_bad_overflow(N: int) -> int:
    count = 0
    fact = 1
    for i in range(1, N+1): #1,2,3,4
        fact *= i
        while fact % 10 == 0:
            count += 1
            fact = int(fact/10)
    return len(str(fact)) + count


@pytest.mark.parametrize(
    ("N", "expected"),
    (
        (5, 3), # 120
        (120, 199),
        (8468, 29586),
    ),
)
def test_digits_in_factorial(
    N: int,
    expected: int
) -> None:
    assert expected == digits_in_factorial(N)
