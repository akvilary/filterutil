# coding=utf-8
"""
Module of collection of OR filters
"""


from .filter_coupling_policy import FilterCouplingPolicy
from .filters import Filters


class OrFilters(Filters):
    """
    Filters collection with OR default coupling policy
    """
    def __init__(
        self,
        default_coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.OR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                FilterCouplingPolicy.OR
                if default_coupling_policy is None
                else default_coupling_policy
            ),
            **kwargs,
        )
