# coding=utf-8
"""
Enum of logic gate
"""

from enum import StrEnum


class LogicGate(StrEnum):
    """
    Enum of logic gate
    """
    AND = 'and'
    OR = 'or'
    XOR = 'xor'
    XNOR = 'xnor'
    NAND = 'nand'
    NOR = 'nor'
