import pytest


def factorial(N: int) -> int:
    res = 1
    for i in range(N):
        res *= (i+1)
    return res

def factorial_recurrsive(N: int) -> int:
    if N == 0:
        return 1

    return N * factorial_recurrsive(N-1)


@pytest.mark.parametrize(
    ("N", "expected"),
    (
        (4, 24),
        (13, 6227020800),
    ),
)
def test_factorial(
    N: int,
    expected: int
) -> None:
    assert expected == factorial(N)
    assert expected == factorial_recurrsive(N)
