"""
Code challenge: palindrome
"""
import re


def palindrome_word(string) -> bool:
    """No dependency"""
    if not str or not isinstance(string, str):
        raise TypeError

    string = string.lower().replace(' ', '')
    reversed_string = ''.join(reversed(string))
    return string == reversed_string


def palindrome_sentence(string) -> bool:
    """No dependency"""
    if not str or not isinstance(string, str):
        raise TypeError

    string = ''.join(re.split(r'[\s!]', string)).lower()
    reversed_string = ''.join(reversed(string))

    return string == reversed_string
