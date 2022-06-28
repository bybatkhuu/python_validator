# -*- coding: utf-8 -*-

try:
    from garlic_validator.validator import validators, checkers, errors
    from garlic_validator.__version__ import __version__
except ImportError:
    from .validator import validators, checkers, errors
    from .__version__ import __version__
