import math

import pytest


# 30 -> (1,30), (2,15), (3,5), (5, 6)
def all_divisors(N: int):
    res = []
    upper = int(math.sqrt(N)) # 30 -> 5.xx
    for i in range(1, upper+1):
        if N%i == 0:
            res.append(i)
            if N/i != i:
                res.append(int(N/i))
    return sorted(res)


def exactly_3_divisors(N: int) -> int:
    def sieve(limit: int) -> list[int]:
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False
        for i in range(2, int(limit**0.5)+1):
            if is_prime[i]:
                for j in range(i*i, limit+1, i):
                    is_prime[j] = False
        return [x for x in range(limit + 1) if is_prime[x]]

    primes = sieve(int(N**0.5))
    res = []
    for p in primes:
        square = p**2
        if square <= N:
            res.append(square)
    return len(res)


@pytest.mark.parametrize(
    ("N", "expected"),
    (
        (6, 1),
        (10, 2),
    ),
)
def test_exactly_3_divisors(
    N: int,
    expected: int
) -> None:
    assert expected == exactly_3_divisors(N)
