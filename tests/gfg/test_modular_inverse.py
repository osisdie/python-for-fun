import pytest


MOD = 1_000_000_007

def modular_inverse(a: int, m: int) -> int:
    for i in range(1, m):
        if (a*i)%m == 1:
            return i
    return -1


@pytest.mark.parametrize(
    ("a", "m", "expected"),
    (
        (3, 11, 4),
        (10, 17, 12),
    ),
)
def test_modular_inverse(
    a: int, m: int,
    expected: int
) -> None:
    assert expected == modular_inverse(a,m)
