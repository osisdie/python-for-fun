"""
Test performance
"""
from functools import lru_cache

import pytest

all_nums = [20]


@pytest.fixture(name='fabi_recursive')
def fixture_fabi_recursive():
    """Regular fabonacci recursive function"""
    def _fabi_recursive(n: int) -> int:
        """Regular fabonacci recursive function"""
        if n in (1, 2):
            return 1
        return _fabi_recursive(n-2) + _fabi_recursive(n-1)

    return _fabi_recursive


@pytest.fixture(name='fabi_non_recursive')
def fixture_fabi_non_recursive():
    """Regular fabonacci non-recursive function"""
    def _fabi_non_recursive(n: int) -> int:
        """Regular fabonacci non-recursive function"""
        if n in (1, 2):
            return 1

        fibs_pre, fibs_cur = 1, 1
        for _ in range(2, n):
            fibs_pre, fibs_cur = fibs_cur, fibs_pre + fibs_cur
        return fibs_cur

    return _fabi_non_recursive


@pytest.fixture(name='fabi_recursive_cached')
def fixture_fabi_recursive_cached():
    """Improved performance of fabonacci recursive function"""
    @lru_cache(maxsize=1000)
    def _fabi_recursive_cached(n: int) -> int:
        if n in (1, 2):
            return 1
        return _fabi_recursive_cached(n-2) + _fabi_recursive_cached(n-1)

    return _fabi_recursive_cached


@pytest.fixture(name='fabi_non_recursive_cached')
def fixture_fabi_non_recursive_cached():
    """Improved performance of fabonacci non-recursive function"""
    @lru_cache(maxsize=1000)
    def _fabi_non_recursive_cached(n: int) -> int:
        """Improved performance of fabonacci non-recursive function"""
        if n in (1, 2):
            return 1

        fibs_pre, fibs_cur = 1, 1
        for _ in range(2, n):
            fibs_pre, fibs_cur = fibs_cur, fibs_pre + fibs_cur
        return fibs_cur

    return _fabi_non_recursive_cached


def my_special_setup():
    """Setup"""


@pytest.fixture(name='number')
def fixture_number():
    """Fabi numbers"""
    return all_nums


@pytest.mark.skip(reason='skip test_perf')
@pytest.mark.parametrize('n', all_nums)
def test_fabi_recursive(benchmark, fabi_recursive, n):
    """basic test cases as benchmark"""
    benchmark.pedantic(
        lambda: fabi_recursive(n=n),
        rounds=10,
        iterations=5,
    )


@pytest.mark.skip(reason='skip test_perf')
@pytest.mark.parametrize('n', all_nums)
def test_fabi_norecursive(benchmark, fabi_non_recursive, n):
    """basic test cases as benchmark"""
    benchmark.pedantic(
        lambda: fabi_non_recursive(n=n),
        rounds=10,
        iterations=5,
    )


# @pytest.mark.skip(reason='skip test_perf')
@pytest.mark.parametrize(
    'fabi_func', [
        pytest.lazy_fixture('fabi_recursive'),  # ranking: 4
        pytest.lazy_fixture('fabi_non_recursive'),  # ranking: 3
        pytest.lazy_fixture('fabi_recursive_cached'),  # ranking: 2
        pytest.lazy_fixture('fabi_non_recursive_cached'),  # ranking: 1
    ],
)
@pytest.mark.parametrize('n', all_nums)
def test_portfolio(benchmark, fabi_func, n):
    """expected high performance test cases compares to benchmark"""
    benchmark.pedantic(
        lambda: fabi_func(n=n),
        iterations=5,
        rounds=10,
    )
