# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import re

from hypothesis import given, strategies as st
import pytest

import strtoolz


def replace_exactly_oracle(s, old, new, count):
    "Simplest implementation, to use as a test reference."
    if count < 0:
        raise ValueError(f'count must be >= 0, not {count}')

    new_s = s.replace(old, new, count)
    found_count = s.count(old)

    if found_count < count:
        raise ValueError(
            f'Only {found_count} occurences could be replaced, required {count}',
        )
    return new_s


@given(
    st.text(),
    st.text(),
    st.text(),
    st.integers(),
)
def test_oracle_equivalence(s, old, new, count):
    try:
        expected = replace_exactly_oracle(s, old, new, count)
        expected_exc = None
    except Exception as exc:
        expected = None
        expected_exc = exc

    if expected is not None:
        actual = strtoolz.replace_exactly(s, old, new, count)
        assert expected == actual
        assert expected_exc is None

    elif expected_exc is not None:
        with pytest.raises(Exception) as actual_excinfo:
            strtoolz.replace_exactly(s, old, new, count)
        assert type(expected_exc) == actual_excinfo.type
        assert actual_excinfo.value.args[0] in expected_exc.args[0]


@given(
    st.text(),
    st.text(),
    st.text(),
    st.integers(max_value=-1),
)
def test_count_arg_range_enforced(s, old, new, count):
    with pytest.raises(ValueError):
        strtoolz.replace_exactly(s, old, new, count)
