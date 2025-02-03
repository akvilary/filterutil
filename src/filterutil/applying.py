# coding=utf-8
"""
Module of applying filters
"""

from typing import Any, Iterable

from .filter_coupling_policy import FilterCouplingPolicy


def apply_filters(
    value: Any,
    filters: Iterable['Filter | CompoundFilter | Filters'],
    coupling_policy: FilterCouplingPolicy = FilterCouplingPolicy.AND,
) -> bool:
    """
    Apply filters to value
    """
    coupling_policy = coupling_policy or FilterCouplingPolicy.AND
    if coupling_policy == FilterCouplingPolicy.AND:
        return apply_filters_with_and_policy(value, filters)
    if coupling_policy == FilterCouplingPolicy.OR:
        return apply_filters_with_or_policy(value, filters)
    if coupling_policy == FilterCouplingPolicy.XOR:
        return apply_filters_with_xor_policy(value, filters)
    raise NotImplementedError(f'FilterCouplingPolicy ({coupling_policy}) is not supported')


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
    Apply with "OR" logic
    """
    for _filter in filters or []:
        if _filter.apply(value):
            return False
    return True
