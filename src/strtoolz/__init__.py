# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

from collections.abc import Iterator
from numbers import Integral
from typing import SupportsIndex, TypeAlias, TypeVar

Bound: TypeAlias = SupportsIndex | None
Str = TypeVar("Str", str, bytes, bytearray)

__all__ = [
    'find_all',
    'find_iter',
]

def find_all(s:Str, sub:Str, start:Bound=None, end:Bound=None) -> list[int]:
    """
    Return a list of all indexes in s where substring sub is found, such that
    none overlap and all substrings are contained within s[start:end].

    Optional arguments start and end are interpreted as in slice.
    """
    return list(find_iter(s, sub, start, end))


def find_iter(s:Str, sub:Str, start:Bound=None, end:Bound=None) -> Iterator[int]:
    """
    Yield all indexes in s where substring sub is found, such that
    none overlap and all substrings are contained within s[start:end].

    Optional arguments start and end are interpreted as in slice.
    """
    stride = max(1, len(sub))
    len_s = len(s)
    while 0 <= (start := s.find(sub, start, end)) <= len_s:
        yield start
        start += stride
