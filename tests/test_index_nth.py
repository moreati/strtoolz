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
def test_str_index_equivalence(s, sub, start, end):
    expected_idx = expected_exc = sentinel = object()
    try:
        expected_idx = str.index(s, sub, start, end)
    except Exception as exc:
        expected_exc = exc

    if expected_idx is not sentinel:
        assert strtoolz.index_nth(s, sub, 0, start, end) == expected_idx
        assert expected_exc is sentinel

    elif expected_exc is not sentinel:
        with pytest.raises(Exception) as actual_excinfo:
            strtoolz.index_nth(s, sub, 0, start, end)
        assert actual_excinfo.type is type(expected_exc)
        assert len(actual_excinfo.value.args) == len(expected_exc.args) == 1
        assert expected_exc.args[0] in actual_excinfo.value.args[0]
        assert expected_idx is sentinel

    else:
        raise Exception('Unexpected branch')


def test_invalid_n():
    with pytest.raises(ValueError): strtoolz.index_nth('', '', n=-1)
    with pytest.raises(ValueError): strtoolz.index_nth('', '', n=2**63)
