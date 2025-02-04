# coding=utf-8
"""
Module of collection of NOR filters
"""


from .filter_coupling_policy import FilterCouplingPolicy
from .filters import Filters


class NorFilters(Filters):
    """
    Filters collection with NOR default coupling policy
    """
    def __init__(
        self,
        default_coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.NOR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                FilterCouplingPolicy.NOR
                if default_coupling_policy is None
                else default_coupling_policy
            ),
            **kwargs,
        )
