# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

"""
strtoolz.find_all() tests

These tests are intended to verify that the relationship
str.find() : strtoolz.find_all() :: re.Pattern.search() : re.Pattern.findall()
holds. We don't wish to duplicate tests of str.find() or re.Pattern.search()
themsolves, instead delegating that to the Python test suite.

There are some cases where {bytearray|bytes|str}.find() & re.Pattern.search()
behaviours differ
1. When the needle is an empty string and the starting position (start or pos
   respectively) is beyond the end of the haystack string

   >>> 'abc'.find('', 4)  # Returns no hit
   -1
   >>> re.compile('').search('abc', pos=4)  # Returns a hit
   <re.Match object; span=(3, 3), match=''>
"""

import re

from hypothesis import assume, given, strategies as st

import strtoolz


@given(
    st.text(),
    st.text(),
    st.integers() | st.none(),
    st.integers() | st.none(),
)
def test_re_findall_equivalence(s, sub, start, end):
    """
    Majority of coverage, except where str.find() and re.Pattern.search()
    behaviour differs.
    """
    assume(start is None or start <= len(s))

    pattern = re.compile(re.escape(sub))
    indexes = [m.start() for m in pattern.finditer(s[start:end])]
    assert indexes == strtoolz.find_all(s, sub, start, end)


def test_empty_sub():
    """
    Belt and braces, already covered but nice to have some concerete examples.
    """
    assert strtoolz.find_all('', '') == [0]
    assert strtoolz.find_all('a', '') == [0, 1]
    assert strtoolz.find_all('ab', '') == [0, 1, 2]

    assert strtoolz.find_all(b'', b'') == [0]
    assert strtoolz.find_all(b'a', b'') == [0, 1]
    assert strtoolz.find_all(b'ab', b'') == [0, 1, 2]

    assert strtoolz.find_all(bytearray(b''), bytearray(b'')) == [0]
    assert strtoolz.find_all(bytearray(b'a'), bytearray(b'')) == [0, 1]
    assert strtoolz.find_all(bytearray(b'ab'), bytearray(b'')) == [0, 1, 2]


def test_empty_sub_start_oob():
    """
    When start > len(s) match str.find() behaviour, not re.Pattern.search().
    """
    assert strtoolz.find_all('', '', start=1) == []
    assert strtoolz.find_all('a', '', start=2) == []
    assert strtoolz.find_all('ab', '', start=3) == []

    assert strtoolz.find_all(b'', b'', start=1) == []
    assert strtoolz.find_all(b'a', b'', start=2) == []
    assert strtoolz.find_all(b'ab', b'', start=3) == []

    assert strtoolz.find_all(bytearray(b''), bytearray(b''), start=1) == []
    assert strtoolz.find_all(bytearray(b'a'), bytearray(b''), start=2) == []
    assert strtoolz.find_all(bytearray(b'ab'), bytearray(b''), start=3) == []
