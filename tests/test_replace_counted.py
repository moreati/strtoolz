# SPDX-FileCopyrightText: 2026 strtoolz authors <https://github.com/moreati/strtoolz>
# SPDX-License-Identifier: MIT

import sys

from hypothesis import given, strategies as st
import pytest

import strtoolz


def replace_counted_oracle(s, old, new, count=1):
    "Simplest implementation, to use as a test reference."
    new_s = s.replace(old, new, count)
    found_count = s.count(old)

    if count < 0:
        count = sys.maxsize
    replaced_count = min(count, found_count)
    return (new_s, replaced_count)


@given(
    st.text(),
    st.text(),
    st.text(),
    st.integers(),
)
def test_oracle_equivalence(s, old, new, count):
    try:
        expected = replace_counted_oracle(s, old, new, count)
        expected_exc = None
    except Exception as exc:
        expected = None
        expected_exc = exc

    if expected is not None:
        actual = strtoolz.replace_counted(s, old, new, count)
        assert expected == actual
        assert expected_exc is None

    if expected_exc is not None:
        assert expected is None
        with pytest.raises(Exception) as actual_excinfo:
            strtoolz.replace_counted(s, old, new, count)
        assert type(expected_exc) == actual_excinfo.type
        assert actual_excinfo.value.args[0] in expected_exc.args[0]


@given(
    st.text(),
    st.text(),
    st.one_of(st.binary(), st.integers(), st.none()),
)
def test_string_args_type_enforced(good1, good2, bad):
    with pytest.raises(TypeError): good1.replace(good2, bad)
    with pytest.raises(TypeError): good1.replace(bad, good2)

    with pytest.raises(TypeError): strtoolz.replace_counted(good1, good2, bad)
    with pytest.raises(TypeError): strtoolz.replace_counted(good1, bad, good2)
    with pytest.raises(TypeError): strtoolz.replace_counted(bad, good1, good2)


@given(
    st.text(),
    st.text(),
    st.text(),
    st.one_of(st.binary(), st.none()),
)
def test_count_arg_type_enforced(s, old, new, count):
    with pytest.raises(TypeError): s.replace(old, new, count)

    with pytest.raises(TypeError): strtoolz.replace_counted(s, old, new, count)

@given(
    st.text(),
    st.text(),
    st.text(),
    st.sampled_from([-2**63-1, 2**63]),
)
def test_count_arg_range_enforced(s, old, new, count):
    with pytest.raises(OverflowError): s.replace(old, new, count)

    with pytest.raises(OverflowError): strtoolz.replace_counted(s, old, new, count)

