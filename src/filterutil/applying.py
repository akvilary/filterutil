# coding=utf-8
"""
Module of applying filters
"""

from functools import reduce
from typing import Any, Iterable

from .filter_coupling_policy import FilterCouplingPolicy


def apply_filters_with_and_policy(
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


def apply_filters_with_or_policy(
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


def apply_filters_with_xor_policy(
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


def apply_filters_with_xnor_policy(
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


def apply_filters_with_nand_policy(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "NAND" logic
    """
    if not filters:
        return False

    return not all(_filter.apply(value) for _filter in filters)


def apply_filters_with_nor_policy(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
):
    """
    Apply with "NOR" logic
    """
    if not filters:
        return True

    return not any(_filter.apply(value) for _filter in filters)


APPLY_FUNC_BY_POLICY = {
    FilterCouplingPolicy.AND: apply_filters_with_and_policy,
    FilterCouplingPolicy.OR: apply_filters_with_or_policy,
    FilterCouplingPolicy.XOR: apply_filters_with_xor_policy,
    FilterCouplingPolicy.XNOR: apply_filters_with_xnor_policy,
    FilterCouplingPolicy.NAND: apply_filters_with_nand_policy,
    FilterCouplingPolicy.NOR: apply_filters_with_nor_policy,
}


def apply_filters(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
    coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.AND,
) -> bool:
    """
    Apply filters to value
    """
    coupling_policy = coupling_policy or FilterCouplingPolicy.AND
    apply_func = APPLY_FUNC_BY_POLICY.get(coupling_policy)
    if apply_func is not None:
        return apply_func(value, filters)
    raise NotImplementedError(f'FilterCouplingPolicy ({coupling_policy}) is not supported')
