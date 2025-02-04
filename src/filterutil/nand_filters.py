# coding=utf-8
"""
Module of collection of NAND filters
"""


from .filter_coupling_policy import FilterCouplingPolicy
from .filters import Filters


class NandFilters(Filters):
    """
    Filters collection with NAND default coupling policy
    """
    def __init__(
        self,
        default_coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.NAND,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                FilterCouplingPolicy.NAND
                if default_coupling_policy is None
                else default_coupling_policy
            ),
            **kwargs,
        )
