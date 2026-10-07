# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import sys

import pytest
from hypothesis import given, strategies as st

import strtoolz


@given(
    st.text(),
    st.text(),
    st.integers() | st.none(),
    st.integers() | st.none(),
)
def test_find_equivalence(s, sub, start, end):
    expected = s.find(sub, start, end)
    assert strtoolz.find_nth(s, sub, n=0, start=start, end=end) == expected


@given(
    st.text(),
    st.text(),
    st.integers(min_value=0, max_value=sys.maxsize),
    st.integers() | st.none(),
    st.integers() | st.none(),
)
def test_find_all_equivalence(s, sub, n, start, end):
    indexes = strtoolz.find_all(s, sub, start=start, end=end)
    actual = strtoolz.find_nth(s, sub, n=n, start=start, end=end)
    try:
        assert actual == indexes[n]
    except IndexError:
        assert actual == -1


def test_invalid_n():
    with pytest.raises(ValueError): strtoolz.find_nth('', '', n=-1)
    with pytest.raises(ValueError): strtoolz.find_nth('', '', n=2**63)
