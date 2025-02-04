# coding=utf-8
"""
Module of collection of XNOR filters
"""


from .logic_gate import LogicGate
from .filters import Filters


class XnorFilters(Filters):
    """
    Filters collection with default XNOR logic gate
    """
    def __init__(
        self,
        default_logic_gate: LogicGate = LogicGate.XNOR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                LogicGate.XNOR
                if default_logic_gate is None
                else default_logic_gate
            ),
            **kwargs,
        )
