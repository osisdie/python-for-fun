"""
Test code challenges
"""
import pytest

from app_package.exam.palindrome.utils import palindrome_word
from app_package.exam.vowel.utils import reverse_vowel


# @pytest.mark.skip(reason='skip test_reverse_vowel')
@pytest.mark.parametrize(
    'test_input, expected', [
        pytest.param('FACEBOOK', 'FOCOBEAK', marks=pytest.mark.basic),
        pytest.param('APPLE', 'EPPLA', marks=pytest.mark.basic),
        pytest.param('FAB', 'FAB', marks=pytest.mark.basic),
        pytest.param('Abc', 'ABC', marks=[pytest.mark.basic, pytest.mark.xfail]),
    ],
)
def test_reverse_vowel(test_input, expected):
    """Positive and negative cases"""
    assert reverse_vowel(test_input) == expected
    # result: bool = reverse_vowel('FACEBOOK')
    # assert result == 'FOCOBEAK'

    # result: bool = reverse_vowel('FAB')
    # assert result == 'FAB'

    # result: bool = reverse_vowel('APPLE')
    # assert result == 'EPPLA'


@pytest.mark.skip(reason='skip test_vowel_corner')
def test_reverse_vowel_corner():
    """Corner cases"""
    result: str = reverse_vowel('')
    assert result == ''

    result: str = reverse_vowel(1)
    assert result is None

    result: str = reverse_vowel([])
    assert result is None

    result: str = reverse_vowel(None)
    assert result is None


# @pytest.mark.skip(reason='skip test_palindrome')
@pytest.mark.parametrize(
    'test_input, expected', [
        pytest.param('aba', True, marks=pytest.mark.basic),
        pytest.param('abba', True, marks=pytest.mark.basic),
        pytest.param('I am a rabbit! tibbaramai', True, marks=pytest.mark.basic),
        pytest.param('abc', True, marks=[pytest.mark.basic, pytest.mark.xfail]),
    ],
)
def test_palindrome(test_input, expected):
    """Positive and negative cases"""
    assert palindrome_word(test_input) == expected
    # result: bool = palindrome_word('aba')
    # assert result is True

    # result: bool = palindrome_word('abba')
    # assert result is True

    # result: bool = palindrome_sentence('I am a rabbit! tibbaramai')
    # assert result is True


@pytest.mark.skip(reason='skip test_palindrome_negative')
def test_palindrome_negative():
    """Negative cases"""
    result: bool = palindrome_word('abc')
    assert result is False


@pytest.mark.skip(reason='skip test_palindrome_corner')
def test_palindrome_corner():
    """Corner cases"""
    result: bool = palindrome_word('')
    assert result is True

    result: bool = palindrome_word(1)
    assert result is False

    result: bool = palindrome_word([])
    assert result is False

    result: bool = palindrome_word(None)
    assert result is False
