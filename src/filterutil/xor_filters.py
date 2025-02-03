# coding=utf-8
"""
Module of collection of XOR filters
"""


from .filter_coupling_policy import FilterCouplingPolicy
from .filters import Filters


class XorFilters(Filters):
    """
    Filters collection with XOR default coupling policy
    """
    def __init__(
        self,
        default_coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.XOR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                FilterCouplingPolicy.XOR
                if default_coupling_policy is None
                else default_coupling_policy
            ),
            **kwargs,
        )
