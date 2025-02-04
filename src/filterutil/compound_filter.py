# coding=utf-8
"""
Module of Compounder
"""

from collections import UserList
from typing import Any, List

from .applying import apply_filters
from .logic_gate import LogicGate


class Compounder:
    """
    Class that implement logic of compounding
    """

    def __and__(self, other) -> 'CompoundFilter':
        return CompoundFilter([self, other], logic_gate=LogicGate.AND)

    def __rand__(self, other) -> 'CompoundFilter':
        return CompoundFilter([other, self], logic_gate=LogicGate.AND)

    def __or__(self, other) -> 'CompoundFilter':
        return CompoundFilter([self, other], logic_gate=LogicGate.OR)

    def __ror__(self, other) -> 'CompoundFilter':
        return CompoundFilter([other, self], logic_gate=LogicGate.OR)

    def __xor__(self, other) -> 'CompoundFilter':
        return CompoundFilter([self, other], logic_gate=LogicGate.XOR)

    def __rxor__(self, other) -> 'CompoundFilter':
        return CompoundFilter([other, self], logic_gate=LogicGate.XOR)

    def xnor(self, other) -> 'CompoundFilter':
        """
        Coupling with XNOR logic
        """
        return CompoundFilter([self, other], logic_gate=LogicGate.XNOR)

    def nand(self, other) -> 'CompoundFilter':
        """
        Coupling with NAND logic
        """
        return CompoundFilter([self, other], logic_gate=LogicGate.NAND)

    def nor(self, other) -> 'CompoundFilter':
        """
        Coupling with NOR logic
        """
        return CompoundFilter([self, other], logic_gate=LogicGate.NOR)


class CompoundFilter(UserList, Compounder):
    """
    Coupling filters
    """

    def __init__(
        self,
        filters: List['Filter | CompoundFilter'],
        *,
        logic_gate: LogicGate = LogicGate.AND,
    ):
        UserList.__init__(self, filters)
        self.logic_gate = logic_gate or LogicGate.AND

    def apply(self, value: Any):
        """
        Apply compound filter
        """
        return apply_filters(value, self, logic_gate=self.logic_gate)
