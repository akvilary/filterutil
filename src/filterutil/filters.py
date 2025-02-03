# coding=utf-8
"""
Module of collection of filters
"""

from collections import UserDict
from typing import Any, List, Optional

from .applying import apply_filters
from .filter_coupling_policy import FilterCouplingPolicy


class Filters(UserDict):
    """
    Filters collection with AND default coupling policy
    """
    def __init__(
        self,
        default_coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.AND,
        /,
        **kwargs,
    ):
        UserDict.__init__(self, **kwargs)
        self.default_coupling_policy = (
            FilterCouplingPolicy.AND
            if default_coupling_policy is None
            else default_coupling_policy
        )

    def apply(
        self,
        value: Any,
        filter_names: Optional[List[str]] = None,
        coupling_policy: Optional[FilterCouplingPolicy] = None,
    ) -> bool:
        """
        Apply all or certain registered filters
        """
        return apply_filters(
            value,
            self.values()
            if filter_names is None
            else [
                self[filter_name]
                for filter_name in filter_names
                if filter_name in self
            ],
            coupling_policy=(
                self.default_coupling_policy
                if coupling_policy is None
                else coupling_policy
            ),
        )

    def apply_and(
        self,
        value: Any,
        filter_names: Optional[List[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "AND" logic
        """
        return self.apply(value, filter_names, coupling_policy=FilterCouplingPolicy.AND)

    def apply_or(
        self,
        value: Any,
        filter_names: Optional[List[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "OR" logic
        """
        return self.apply(value, filter_names, coupling_policy=FilterCouplingPolicy.OR)

    def apply_xor(
        self,
        value: Any,
        filter_names: Optional[List[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "XOR" logic
        """
        return self.apply(value, filter_names, coupling_policy=FilterCouplingPolicy.XOR)
