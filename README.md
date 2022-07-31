# Python Validator (garlic_validator)

Cerberus and validator-collection based custom validator package (garlic_validator) for python projects.

## Features

* Validator-collection based validator - [https://pypi.org/project/validator-collection](https://pypi.org/project/validator-collection)
* Cerberus schema validation - [https://pypi.org/project/Cerberus](https://pypi.org/project/Cerberus)
* Pydantic validation - [https://pypi.org/project/pydantic](https://pypi.org/project/pydantic)
* Custom validator module
* is_empty, is_numpy, is_tensor, is_float, is_truthy, is_falsy, is_bool, is_attr_empty

---

## Installation

### 1. Prerequisites

* **Python (>= v3.7)**
* **PyPi (>= v21)**

### 2. Install garlic-validator

#### A. [RECOMMENDED] PyPi install

```sh
# Install or upgrade garlic-validator package:
pip install --upgrade garlic-validator

# To uninstall package:
pip uninstall -y garlic-validator
```

#### B. Manually add to PYTHONPATH (Recommended for development)

```sh
# Clone repository by git:
git clone https://github.com/bybatkhuu/python_validator.git garlic_validator
cd garlic_validator

# Install python dependencies:
pip install --upgrade pip
cat requirements.txt | xargs -n 1 -L 1 pip install --no-cache-dir

# Add current path to PYTHONPATH:
export PYTHONPATH="${PWD}:${PYTHONPATH}"
```

#### C. Manually compile and setup (Not recommended)

```sh
# Clone repository by git:
git clone https://github.com/bybatkhuu/python_validator.git garlic_validator
cd garlic_validator

# Building python package:
pip install --upgrade pip setuptools wheel
python setup.py build
# Install python dependencies with built package to current python environment:
python setup.py install --record installed_files.txt

# To remove only installed garlic-validator package:
head -n 1 installed_files.txt | xargs rm -vrf
# Or to remove all installed files and packages:
cat installed_files.txt | xargs rm -vrf
```

## Usage/Examples

**garlic-validator** and **validator-collection**:

```python
import numpy as np
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

is_empty = checkers.is_empty(np.array([]))
# True


## is_numpy(val)
is_numpy = checkers.is_numpy(np.array([]))
# True

is_numpy = checkers.is_numpy(np.array([1, 2, 3]))
# True

is_numpy = checkers.is_numpy(None)
# False


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

is_bool = checkers.is_bool('1', coerce_value=True)
# True

is_bool = checkers.is_bool('NO', coerce_value=True)
# True
```

**Cerberus**:

```python
from cerberus import Validator

v = Validator({ 'name': { 'type': 'string' } })
print(v.validate({ 'name': 'john doe' }))
# True

v.schema = {'amount': {'type': 'integer'}}
print(v.validate({'amount': '1'}))
# False
print(v.errors)
# {'amount': ['must be of integer type']}

v.schema = {'amount': {'type': 'integer', 'coerce': int}}
print(v.validate({'amount': '1'}))
# True
print(v.document)
# {'amount': 1}

to_bool = lambda v: v.lower() in ('true', '1')
v.schema = {'flag': {'type': 'boolean', 'coerce': (str, to_bool)}}
print(v.validate({'flag': 'true'}))
# True
print(v.document)
# {'flag': True}
```

**pydantic**:

```python
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
```

---

## Running Tests

To run tests, run the following command:

```sh
pytest
```

---

## References

* [https://validator-collection.readthedocs.io/en/latest/index.html](https://validator-collection.readthedocs.io/en/latest/index.html)
* [https://github.com/insightindustry/validator-collection](https://github.com/insightindustry/validator-collection)
* [https://pydantic-docs.helpmanual.io](https://pydantic-docs.helpmanual.io)
* [https://github.com/samuelcolvin/pydantic](https://github.com/samuelcolvin/pydantic)
* [https://docs.python-cerberus.org/en/stable](https://docs.python-cerberus.org/en/stable)
* [https://github.com/pyeve/cerberus](https://github.com/pyeve/cerberus)
