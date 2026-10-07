# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import itertools
import sys
from collections.abc import Iterator
from numbers import Integral
from typing import SupportsIndex, TypeAlias, TypeVar

Bound: TypeAlias = SupportsIndex | None
Str = TypeVar("Str", str, bytes, bytearray)

__all__ = [
    'find_all',
    'find_iter',
    'find_nth',
    'index_nth',
]

def find_all(s:Str, sub:Str, /, start:Bound=None, end:Bound=None) -> list[int]:
    """
    Return a list of all indexes in string s where substring sub is found,
    with no overlaps and all substrings contained within s[start:end].

    Optional arguments start and end are interpreted as in slice notation.
    """
    return list(find_iter(s, sub, start, end))


def find_iter(s:Str, sub:Str, /, start:Bound=None, end:Bound=None) -> Iterator[int]:
    """
    Yield all indexes in string s where substring sub is found,
    with no overlaps and all substrings contained within s[start:end].

    Optional arguments start and end are interpreted as in slice notation.
    """
    stride = max(1, len(sub))
    while 0 <= (start := s.find(sub, start, end)):
        yield start
        start += stride


def find_nth(s:Str, sub:Str, /, n:int, start:Bound=None, end:Bound=None) -> int:
    """
    Return the index of the nth non-overlapping occurence of substring sub
    within s[start:end], otherwise -1.

    n is 0-based, as though indexing into the list returned by find_all().
    Optional arguments start and end are interpreted as in slice notation.
    """
    if not 0 <= n <= sys.maxsize:
        raise ValueError('n must be an integer 0 <= n <= sys.maxsize, got: {n}')
    it = find_iter(s, sub, start=start, end=end)
    return next(itertools.islice(it, n, None), -1)


def index_nth(s:Str, sub:Str, /, n:int, start:Bound=None, end:Bound=None) -> int:
    """
    Like find_nth(), but raise ValueError when the nth substring is not found.
    """
    idx = find_nth(s, sub, n=n, start=start, end=end)
    if idx < 0:
        raise ValueError('nth substring not found')
    return idx
