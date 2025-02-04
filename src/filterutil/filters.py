# coding=utf-8
"""
Module of collection of filters
"""

from collections import UserDict
from typing import Any, Optional, Iterable

from .applying import apply_filters
from .logic_gate import LogicGate


class Filters(UserDict):
    """
    Filters collection with default AND logic gate
    """
    def __init__(
        self,
        default_logic_gate: LogicGate = LogicGate.AND,
        /,
        **kwargs,
    ):
        UserDict.__init__(self, **kwargs)
        self.default_logic_gate = (
            LogicGate.AND
            if default_logic_gate is None
            else default_logic_gate
        )

    def apply(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
        logic_gate: Optional[LogicGate] = None,
    ) -> bool:
        """
        Apply all or certain registered filters
        """
        return apply_filters(
            value,
            self.values()
            if filter_names is None
            else [
                self[filter_name]
                for filter_name in filter_names
                if filter_name in self
            ],
            logic_gate=(
                self.default_logic_gate
                if logic_gate is None
                else logic_gate
            ),
        )

    def apply_and(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "AND" logic
        """
        return self.apply(value, filter_names, logic_gate=LogicGate.AND)

    def apply_or(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "OR" logic
        """
        return self.apply(value, filter_names, logic_gate=LogicGate.OR)

    def apply_xor(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "XOR" logic
        """
        return self.apply(value, filter_names, logic_gate=LogicGate.XOR)

    def apply_xnor(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "XNOR" logic
        """
        return self.apply(value, filter_names, logic_gate=LogicGate.XNOR)

    def apply_nand(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "NAND" logic
        """
        return self.apply(value, filter_names, logic_gate=LogicGate.NAND)

    def apply_nor(
        self,
        value: Any,
        filter_names: Optional[Iterable[str]] = None,
    ) -> bool:
        """
        Apply all or certain registered filters with "NOR" logic
        """
        return self.apply(value, filter_names, logic_gate=LogicGate.NOR)
