"""
Code challenge: reverse vowels
"""
from typing import List


def reverse_vowel(string) -> str:
    """No dependency"""
    if not str or not isinstance(string, str):
        raise TypeError

    vowel: List[str] = []
    for s1 in string:
        if s1 in 'aeiouAEIOU':
            vowel.append(s1)

    vowel_len: int = len(vowel)
    vowel_idx: int = 1
    res: List[str] = []
    for s in string:
        if s in 'aeiouAEIOU':
            res.append(vowel[-(vowel_idx % vowel_len)])
            vowel_idx += 1
        else:
            res.append(s)

    return ''.join(res)
