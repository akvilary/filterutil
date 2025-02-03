# coding=utf-8
"""
Module of Compounder
"""

from collections import UserList
from typing import Any, List

from .applying import apply_filters
from .filter_coupling_policy import FilterCouplingPolicy


class Compounder:
    """
    Class that implement logic of compounding
    """

    def __and__(self, other) -> 'CompoundFilter':
        return CompoundFilter([self, other], coupling_policy=FilterCouplingPolicy.AND)

    def __rand__(self, other) -> 'CompoundFilter':
        return CompoundFilter([other, self], coupling_policy=FilterCouplingPolicy.AND)

    def __or__(self, other) -> 'CompoundFilter':
        return CompoundFilter([self, other], coupling_policy=FilterCouplingPolicy.OR)

    def __ror__(self, other) -> 'CompoundFilter':
        return CompoundFilter([other, self], coupling_policy=FilterCouplingPolicy.OR)

    def __xor__(self, other) -> 'CompoundFilter':
        return CompoundFilter([self, other], coupling_policy=FilterCouplingPolicy.XOR)

    def __rxor__(self, other) -> 'CompoundFilter':
        return CompoundFilter([other, self], coupling_policy=FilterCouplingPolicy.XOR)


class CompoundFilter(UserList, Compounder):
    """
    Coupling filters
    """

    def __init__(
        self,
        filters: List['Filter | CompoundFilter'],
        *,
        coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.AND,
    ):
        UserList.__init__(self, filters)
        self.coupling_policy = coupling_policy or FilterCouplingPolicy.AND

    def apply(self, value: Any):
        """
        Apply compound filter
        """
        return apply_filters(value, self, coupling_policy=self.coupling_policy)  # pylint: disable=protected-access
