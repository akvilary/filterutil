# coding=utf-8
"""
Module of collection of XNOR filters
"""


from .filter_coupling_policy import FilterCouplingPolicy
from .filters import Filters


class XnorFilters(Filters):
    """
    Filters collection with XNOR default coupling policy
    """
    def __init__(
        self,
        default_coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.XNOR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                FilterCouplingPolicy.XNOR
                if default_coupling_policy is None
                else default_coupling_policy
            ),
            **kwargs,
        )
