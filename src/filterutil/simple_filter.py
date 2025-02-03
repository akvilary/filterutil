# coding=utf-8
"""
Module of Filter
"""

from typing import Any, Callable

from .compound_filter import Compounder


# pylint: disable=too-few-public-methods
class Filter(Compounder):
    """
    Class of single filter
    """

    def __init__(self, validator: Callable, *args, **kwargs):
        self.validator = validator
        self.args = args
        self.kwargs = kwargs

    def apply(self, value: Any) -> bool:
        """
        Apply the filter for given value
        """
        return self.validator(value, *self.args, **self.kwargs)
