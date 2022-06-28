# -*- coding: utf-8 -*-

import pytest
import numpy as np

from garlic_validator import validators, checkers, errors


@pytest.mark.parametrize('value, trim_str, expected', [
    ('', None, True),
    (' ', True, True),
    (None, None, True),
    ([], None, True),
    ({}, None, True),
    ((), None, True),
    (set(), None, True),
    (range(0), None, True),
    (np.array([]), None, True),
    ('Not empty!', None, False),
    (' ', None, False),
    (123, None, False),
    ([1, 2, 3], None, False),
    ({ 'name': '' }, None, False),
    (set([1, 2, 3]), None, False),
    (range(3), None, False),
    (np.array([1, 2.3, 4]), None, False)
])
def test_is_emtpy(value, trim_str, expected):
    result = None
    if trim_str:
        result = checkers.is_empty(value, trim_str)
    else:
        result = checkers.is_empty(value)
    assert result == expected


@pytest.mark.parametrize('value, expected', [
    (np.array([1, 2, 3.4]), True),
    (np.array([]), True),
    ([1.1, 2, 3], False),
    (1.23, False),
    ('np.array([1, 2, 3])', False),
    (None, False)
])
def test_is_numpy(value, expected):
    assert checkers.is_numpy(value) == expected


@pytest.mark.parametrize('value, expected', [
    (0, True),
    (1.0, True),
    (1.123, True),
    (-2.12, True),
    (+123.0001, True),
    (1e+123, True),
    ('123', True),
    ('123.123', True),
    ('0123.000', True),
    ('1e+12', True),
    (None, False),
    ('', False),
    (' ', False),
    ([], False),
    ([1, 2.3], False),
    ('123_123', False),
    ('123asd', False),
    ('123+asd', False)
])
def test_is_float(value, expected):
    assert checkers.is_float(value) == expected


@pytest.mark.parametrize('value, expected', [
    (True, True),
    (1, True),
    ('1', True),
    ('1.0', True),
    ('TRUE', True),
    ('True', True),
    ('true', True),
    ('YES', True),
    ('Yes', True),
    ('yes', True),
    ('Y', True),
    ('y', True),
    (False, False),
    ('a', False),
    (1.1, False),
    ([1], False)
])
def test_is_truthy(value, expected):
    assert checkers.is_truthy(value) == expected


@pytest.mark.parametrize('value, expected', [
    (False, True),
    (0, True),
    ('0', True),
    ('0.0', True),
    ('FALSE', True),
    ('False', True),
    ('false', True),
    ('NO', True),
    ('No', True),
    ('no', True),
    ('N', True),
    ('n', True),
    (True, False),
    ('abc', False),
    (2, False),
    ([1, 2], False)
])
def test_is_falsy(value, expected):
    assert checkers.is_falsy(value) == expected


@pytest.mark.parametrize('value, coerce_value, expected', [
    (True, None, True),
    (False, None, True),
    (1, None, False),
    ('True', None, False),
    (None, None, False),
    ([True, False], None, False),
    (0, True, True),
    ('YES', True, True),
    ('n', True, True),
])
def test_is_bool(value, coerce_value, expected):
    result = None
    if coerce_value:
        result = checkers.is_bool(value, coerce_value)
    else:
        result = checkers.is_bool(value)
    assert result == expected
