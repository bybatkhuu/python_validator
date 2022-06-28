#!/usr/bin/env python
# -*- coding: utf-8 -*-

from garlic_validator import validators, checkers, errors


try:
    email_address = validators.email('test@domain.dev')
    # The value of email_address will now be "test@domain.dev"

    email_address = validators.email('this-is-an-invalid-email')
    # Will raise a ValueError

    email_address = validators.email(None)
    # Will raise an EmptyValueError
except errors.EmptyValueError:
    # Handling logic goes here
    print('Email address is empty')
except errors.InvalidEmailError:
    # More handlign logic goes here
    print('Invalid email address')

email_address = validators.email(None, allow_empty=True)
print(email_address)
# The value of email_address will now be None

email_address = validators.email('', allow_empty=True)
print(email_address)
# The value of email_address will now be None

is_email_address = checkers.is_email('test@domain.dev')
print(is_email_address)
# The value of is_email_address will now be True

is_email_address = checkers.is_email('this-is-an-invalid-email')
print(is_email_address)
# The value of is_email_address will now be False

is_email_address = checkers.is_email(None)
print(is_email_address)
# The value of is_email_address will now be False


## Custom validators:
## is_empty(val, trim_str=False)
is_empty = checkers.is_empty(None)
# True

is_empty = checkers.is_empty('')
# True

is_empty = checkers.is_empty('    ')
# False

is_empty = checkers.is_empty('    ', trim_str=True)
# True

is_empty = checkers.is_empty([])
# True

is_empty = checkers.is_empty({})
# True

is_empty = checkers.is_empty(())
# True

is_empty = checkers.is_empty(set())
# True

is_empty = checkers.is_empty(range(0))
# True


## is_float(val)
is_float = checkers.is_float(1)
# True

is_float = checkers.is_float(-1.1123)
# True

is_float = checkers.is_float(1e+123)
# True

is_float = checkers.is_float('0123.000')
# True

is_float = checkers.is_float('1e+12')
# True

is_float = checkers.is_float('2002_12')
# False


## is_truthy(val)
is_truthy = checkers.is_truthy(True)
# True

is_truthy = checkers.is_truthy(1)
# True

is_truthy = checkers.is_truthy('1')
# True

is_truthy = checkers.is_truthy('1.0')
# True

is_truthy = checkers.is_truthy('TRUE')
# True

is_truthy = checkers.is_truthy('True')
# True

is_truthy = checkers.is_truthy('true')
# True

is_truthy = checkers.is_truthy('YES')
# True

is_truthy = checkers.is_truthy('Yes')
# True

is_truthy = checkers.is_truthy('yes')
# True

is_truthy = checkers.is_truthy('Y')
# True

is_truthy = checkers.is_truthy('y')
# True

is_truthy = checkers.is_truthy(1.1)
# False

is_truthy = checkers.is_truthy([1])
# False

is_truthy = checkers.is_truthy(False)
# False


## is_falsy(val)
is_falsy = checkers.is_falsy(False)
# True

is_falsy = checkers.is_falsy(0)
# True

is_falsy = checkers.is_falsy('0')
# True

is_falsy = checkers.is_falsy('0.0')
# True

is_falsy = checkers.is_falsy('FALSE')
# True

is_falsy = checkers.is_falsy('False')
# True

is_falsy = checkers.is_falsy('false')
# True

is_falsy = checkers.is_falsy('NO')
# True

is_falsy = checkers.is_falsy('No')
# True

is_falsy = checkers.is_falsy('no')
# True

is_falsy = checkers.is_falsy('N')
# True

is_falsy = checkers.is_falsy('n')
# True

is_falsy = checkers.is_falsy(2)
# False

is_falsy = checkers.is_falsy('a')
# False

is_falsy = checkers.is_falsy(True)
# False


## is_bool(val, coerce_value=False)
is_bool = checkers.is_bool(True)
# True

is_bool = checkers.is_bool(False)
# True

is_bool = checkers.is_bool(1)
# False

is_bool = checkers.is_bool('False', coerce_value=True)
# True

is_bool = checkers.is_bool('1', coerce_value=True)
# True

is_bool = checkers.is_bool('NO', coerce_value=True)
# True
