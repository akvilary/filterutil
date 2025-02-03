import pytest
from filterutil import Filter, Filters, OrFilters, FilterCouplingPolicy


def test_or_filters_init():
    filters = OrFilters()
    assert isinstance(filters, Filters)


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, False),
    ],
)
def test_or_filters_filtering(value, filters_dict, expected_result):
    filters = OrFilters(**filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, False),
    ],
)
def test_or_filters_setitem(value, filters_dict, expected_result):
    filters = OrFilters()
    for k, v in filters_dict.items():
        filters[k] = v
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, False),
    ],
)
def test_or_filters_update(value, filters_dict, expected_result):
    filters = OrFilters()
    filters.update(filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, False),
    ],
)
def test_filters_as_or(value, filters_dict, expected_result):
    filters = Filters(
        FilterCouplingPolicy.OR,
        **filters_dict,
    )
    assert filters.apply(value) == expected_result
