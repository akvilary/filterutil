# coding=utf-8
"""
Module of collection of XOR filters
"""


from .logic_gate import LogicGate
from .filters import Filters


class XorFilters(Filters):
    """
    Filters collection with default XOR logic gate
    """
    def __init__(
        self,
        default_logic_gate: LogicGate = LogicGate.XOR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                LogicGate.XOR
                if default_logic_gate is None
                else default_logic_gate
            ),
            **kwargs,
        )
