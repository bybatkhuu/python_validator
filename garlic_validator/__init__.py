# -*- coding: utf-8 -*-

try:
    from garlic_validator.validator import validators, checkers, errors, __version__
except ImportError:
    from .validator import validators, checkers, errors, __version__
