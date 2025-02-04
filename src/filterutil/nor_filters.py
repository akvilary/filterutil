# coding=utf-8
"""
Module of collection of NOR filters
"""


from .logic_gate import LogicGate
from .filters import Filters


class NorFilters(Filters):
    """
    Filters collection with default NOR logic gate
    """
    def __init__(
        self,
        default_logic_gate: LogicGate = LogicGate.NOR,
        /,
        **kwargs,
    ):
        Filters.__init__(
            self,
            (
                LogicGate.NOR
                if default_logic_gate is None
                else default_logic_gate
            ),
            **kwargs,
        )
