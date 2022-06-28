#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pydantic import validate_arguments, ValidationError


@validate_arguments
def repeat(s: str, count: int, *, separator: bytes = b'') -> bytes:
    b = s.encode()
    return separator.join(b for _ in range(count))


a = repeat('hello', 3)
print(a)
#> b'hellohellohello'

b = repeat('x', '4', separator=' ')
print(b)
#> b'x x x x'

try:
    c = repeat('hello', 'wrong')
except ValidationError as exc:
    print(exc)
    """
    1 validation error for Repeat
    count
      value is not a valid integer (type=type_error.integer)
    """
