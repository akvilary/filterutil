# coding=utf-8
"""
Module of applying filters
"""

from functools import reduce
from typing import Any, Iterable

from .logic_gate import LogicGate


def apply_filters_and(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "AND" logic
    """
    for _filter in filters or []:
        if not _filter.apply(value):
            return False
    return True


def apply_filters_or(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "OR" logic
    """
    if not filters:
        return True
    for _filter in filters:
        if _filter.apply(value):
            return True
    return False


def apply_filters_xor(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "XOR" logic
    """
    if not filters:
        return True

    iterator = iter(filters)
    return reduce(
        lambda result, _filter: result ^ _filter.apply(value),
        iterator,
        next(iterator).apply(value),
    )


def apply_filters_xnor(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "XNOR" logic
    """
    if not filters:
        return True

    iterator = iter(filters)
    return reduce(
        lambda result, _filter: result is _filter.apply(value),
        iterator,
        next(iterator).apply(value),
    )


def apply_filters_nand(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "NAND" logic
    """
    if not filters:
        return False

    return not all(_filter.apply(value) for _filter in filters)


def apply_filters_nor(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "NOR" logic
    """
    if not filters:
        return True

    return not any(_filter.apply(value) for _filter in filters)


APPLY_FUNC_BY_LOGIC_GATE = {
    LogicGate.AND: apply_filters_and,
    LogicGate.OR: apply_filters_or,
    LogicGate.XOR: apply_filters_xor,
    LogicGate.XNOR: apply_filters_xnor,
    LogicGate.NAND: apply_filters_nand,
    LogicGate.NOR: apply_filters_nor,
}


def apply_filters(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
    logic_gate: LogicGate = LogicGate.AND,
) -> bool:
    """
    Apply filters to value
    """
    logic_gate = logic_gate or LogicGate.AND
    apply_func = APPLY_FUNC_BY_LOGIC_GATE.get(logic_gate)
    if apply_func is not None:
        return apply_func(value, filters)
    raise NotImplementedError(f'Logic gate ({logic_gate}) is not supported')
