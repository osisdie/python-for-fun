"""
Test environment variables as config
"""
import pytest

from app_package.settings import RuntimeEnv


@pytest.mark.parametrize(
    'test_input, expected', [
        pytest.param(RuntimeEnv.SDK_ENV, 'dev', marks=pytest.mark.basic),
        pytest.param(RuntimeEnv.SDK_ENV, 'prod', marks=[pytest.mark.basic, pytest.mark.xfail]),
    ],
)
def test_config(test_input, expected):
    """Positive and negative cases"""
    assert test_input is not None
    assert test_input == expected
    # assert RuntimeEnv is not None
    # assert RuntimeEnv.SDK_ENV == 'dev'


@pytest.mark.skip(reason='skip test_negative')
def test_negative():
    """Negative cases"""
    assert RuntimeEnv is not None
    assert RuntimeEnv.SDK_ENV != 'prod'
