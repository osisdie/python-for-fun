import pytest


MOD = 1_000_000_007

def multiply_under_modulo(a: int, b: int) -> int:
    return ( a%MOD * b%MOD ) % MOD


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    (
        (1000000007, 1000000007, 0),
        (92233720368547758, 92233720368547758, 484266119),
    ),
)
def test_multiply_under_modulo(
    a: int, b: int,
    expected: int
) -> None:
    assert expected == multiply_under_modulo(a,b)
