import pytest
from filterutil import Filter, Filters, FilterCouplingPolicy


def test_filters_init():
    filters = Filters()
    assert isinstance(filters, Filters)
    assert filters.default_coupling_policy == FilterCouplingPolicy.AND


def test_filters_init_with_none():
    filters = Filters(None)
    assert isinstance(filters, Filters)
    assert filters.default_coupling_policy == FilterCouplingPolicy.AND


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 1), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_filters_filtering(value, filters_dict, expected_result):
    filters = Filters(**filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 1), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_filters_setitem(value, filters_dict, expected_result):
    filters = Filters()
    for k, v in filters_dict.items():
        filters[k] = v
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 1), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_filters_update(value, filters_dict, expected_result):
    filters = Filters()
    filters.update(filters_dict)
    assert filters.apply(value) == expected_result
