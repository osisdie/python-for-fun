import pytest


MOD = 1_000_000_007

def addition_under_modulo(a: int, b: int) -> int:
    return ( a + b ) % MOD


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    (
        (1000000007, 1000000007, 0),
        (9223372036854775807, 9223372036854775807, 582344006),
    ),
)
def test_addition_under_modulo(
    a: int, b: int,
    expected: int
) -> None:
    assert expected == addition_under_modulo(a,b)
