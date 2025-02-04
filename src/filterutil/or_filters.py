# coding=utf-8
"""
Module of collection of OR filters
"""


from .logic_gate import LogicGate
from .filters import Filters


class OrFilters(Filters):
    """
    Filters collection with default OR logic gate
    """
    def __init__(
        self,
        default_logic_gate: LogicGate = LogicGate.OR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                LogicGate.OR
                if default_logic_gate is None
                else default_logic_gate
            ),
            **kwargs,
        )
