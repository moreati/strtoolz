# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import re
import sys

from hypothesis import given, strategies as st
import pytest

import strtoolz

@given(
    st.text(),
    st.text(),
)
def test_n0_equivalence(s, sep):
    try:
        expected = s.partition(sep)
        expected_exc = None
    except Exception as exc:
        expected = None
        expected_exc = exc

    if expected is not None:
        actual = strtoolz.partition_nth(s, sep, n=0)
        assert expected == actual
        assert expected_exc is None

    elif expected_exc is not None:
        with pytest.raises(Exception) as actual_excinfo:
            strtoolz.partition_nth(s, sep, n=0)
        assert type(expected_exc) == actual_excinfo.type
        assert actual_excinfo.value.args[0] == expected_exc.args[0]


@given(
    st.text(),
    st.text(),
    st.text(),
    st.integers(max_value=-1),
)
def test_n_arg_range_enforced(s, old, new, count):
    with pytest.raises(ValueError):
        strtoolz.replace_nth(s, old, new, count)
