#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
