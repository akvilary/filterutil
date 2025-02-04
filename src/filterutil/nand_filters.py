# coding=utf-8
"""
Module of collection of NAND filters
"""


from .logic_gate import LogicGate
from .filters import Filters


class NandFilters(Filters):
    """
    Filters collection with default NAND logic gate
    """
    def __init__(
        self,
        default_logic_gate: LogicGate = LogicGate.NAND,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                LogicGate.NAND
                if default_logic_gate is None
                else default_logic_gate
            ),
            **kwargs,
        )
