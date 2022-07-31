# -*- coding: utf-8 -*-

import logging

from pydantic import validate_arguments
from validator_collection import validators, checkers, errors

from .__version__ import __version__

logger = logging.getLogger(__name__)


@validate_arguments
def is_empty(value, trim_str: bool=False):
    """Check 'value' is empty or not.
    Works for None, value == '', len(value) == 0, and val.size == 0.

    Args:
        value    (any , required): The value to check.
        trim_str (bool, optional): If 'value' is string, trim white spaces by strip() function. Defaults to False.

    Returns:
        bool: True when empty, False for not empty.
    """

    if value is None:
        return True

    if isinstance(value, str):
        if trim_str:
            value = value.strip()

        if value == '':
            return True

    elif isinstance(value, list) or isinstance(value, dict) or isinstance(value, tuple) or isinstance(value, range) or isinstance(value, set):
        if len(value) == 0:
            return True

    if is_numpy(value):
        if value.size == 0:
            return True

    if is_tensor(value):
        if value.nelement() == 0:
            return True

    return False


@validate_arguments
def is_numpy(value):
    """Check 'value' is numpy array or not.

    Args:
        value (any, required): The value to check.

    Returns:
        bool: True if 'value' is valid, False if it is not.
    """

    if f"{type(value).__module__}.{type(value).__name__}" == 'numpy.ndarray':
        return True

    return False


@validate_arguments
def is_tensor(value):
    """Check 'value' is torch.Tensor or not.

    Args:
        value (any, required): The value to check.

    Returns:
        bool: True if 'value' is valid, False if it is not.
    """

    if f"{type(value).__module__}.{type(value).__name__}" == 'torch.Tensor':
        return True

    return False


@validate_arguments
def is_float(value, minimum=None, maximum=None, **kwargs):
    """Check 'value' is a float or not.

    Args:
        value   (any    , required): The value to check.
        minimum (numeric, optional): If supplied, will make sure that 'value' is greater than or equal to this value. Defaults to None.
        maximum (numeric, optional): If supplied, will make sure that 'value' is less than or equal to this value. Defaults to None.

    Raises:
        error: If 'kwargs' contains duplicate keyword parameters or duplicates keyword parameters passed to the underlying validator.

    Returns:
        bool: True if 'value' is valid, False if it is not.
    """

    if isinstance(value, str):
        if '_' in value:
            return False

    try:
        validators.float(value, minimum, maximum, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False

    return True


@validate_arguments
def is_truthy(value):
    """Check 'value' is Truthy or not (possible to parse into boolean).

    Args:
        value (any, required): The value to check.

    Returns:
        bool: True if 'value' is valid, False if it is not.
    """

    if value in [True, 1, '1', '1.0', 'TRUE', 'True', 'true', 'YES', 'Yes', 'yes', 'Y', 'y']:
        return True
    else:
        return False


@validate_arguments
def is_falsy(value):
    """Check 'value' is Falsy or not (possible to parse into boolean).

    Args:
        value (any, required): The value to check.

    Returns:
        bool: True if 'value' is valid, False if it is not.
    """

    if value in [False, 0, '0', '0.0', 'FALSE', 'False', 'false', 'NO', 'No', 'no', 'N', 'n']:
        return True
    else:
        return False


@validate_arguments
def is_bool(value, coerce_value: bool=False):
    """Check 'value' is boolean or not.

    Args:
        value        (any , required): The value to check.
        coerce_value (bool, optional): If True supplied, indicate 'value' is convertable into boolean. Defaults to False.

    Returns:
        bool: True if 'value' is valid, False if it is not.
    """

    if isinstance(value, bool):
        return True

    if coerce_value:
        if is_truthy(value) or is_falsy(value):
            return True

    return False


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def is_attr_empty(obj: object, attr_name: str):
    """Empty checker method for object attribute.

    Args:
        obj       (object, required): Any object.
        attr_name (str   , required): Object's attibute name to check.

    Returns:
        bool: True when attribute is empty, False for not empty.
    """

    try:
        if (not isinstance(obj, dict)) and is_empty(obj):
            raise ValueError("'obj' argument value is empty!")

        attr_name = attr_name.strip()
        if is_empty(attr_name):
            raise ValueError("'attr_name' argument value is empty!")
    except ValueError as err:
        logger.exception(err)
        raise

    if isinstance(obj, dict):
        if len(obj) == 0:
            return True

        if not attr_name in obj:
            return True

        _val = obj[attr_name]
        if is_empty(_val):
            return True
        return False

    try:
        _val = getattr(obj, attr_name)
    except AttributeError:
        return True

    if is_empty(_val):
        return True
    return False


checkers.is_empty = is_empty
checkers.is_numpy = is_numpy
checkers.is_tensor = is_tensor
checkers.is_float = is_float
checkers.is_truthy = is_truthy
checkers.is_falsy = is_falsy
checkers.is_bool = is_bool
checkers.is_attr_empty = is_attr_empty
