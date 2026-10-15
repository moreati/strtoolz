# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import re
import sys

from hypothesis import given, strategies as st
import pytest

import strtoolz


def replace_nth_oracle(s, old, new, n):
    "Simplest implementation, to use as a test reference."
    if not 0 <= n <= sys.maxsize:
        raise ValueError('n must be an integer 0 <= n <= sys.maxsize, got: {n}')

    pattern = re.compile(re.escape(old))
    for i, match in enumerate(pattern.finditer(s)):
        if i != n:
            continue
        return s[0:0].join([s[:match.start()], new, s[match.end():]])

    raise ValueError('nth occurrence of old substring not found')


@given(
    st.text(),
    st.text(),
    st.text(),
    st.integers(),
)
def test_oracle_equivalence(s, old, new, n):
    try:
        expected = replace_nth_oracle(s, old, new, n=n)
        expected_exc = None
    except Exception as exc:
        expected = None
        expected_exc = exc

    if expected is not None:
        actual = strtoolz.replace_nth(s, old, new, n=n)
        assert expected == actual
        assert expected_exc is None

    elif expected_exc is not None:
        with pytest.raises(Exception) as actual_excinfo:
            strtoolz.replace_nth(s, old, new, n=n)
        assert type(expected_exc) == actual_excinfo.type
        assert actual_excinfo.value.args[0] in expected_exc.args[0]


@given(
    st.text(),
    st.text(),
    st.text(),
    st.integers(max_value=-1),
)
def test_n_arg_range_enforced(s, old, new, count):
    with pytest.raises(ValueError):
        strtoolz.replace_nth(s, old, new, count)
