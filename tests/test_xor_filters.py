import pytest
from filterutil import Filter, Filters, XorFilters, FilterCouplingPolicy


def test_xor_filters_init():
    filters = XorFilters()
    assert isinstance(filters, Filters)


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_xor_filters_filtering(value, filters_dict, expected_result):
    filters = XorFilters(**filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_xor_filters_setitem(value, filters_dict, expected_result):
    filters = XorFilters()
    for k, v in filters_dict.items():
        filters[k] = v
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_xor_filters_update(value, filters_dict, expected_result):
    filters = XorFilters()
    filters.update(filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, str))}, True),
        (1, {'a': Filter(lambda x: x == 2), 'b': Filter(lambda x: isinstance(x, int))}, False),
    ],
)
def test_filters_as_xor(value, filters_dict, expected_result):
    filters = Filters(
        FilterCouplingPolicy.XOR,
        **filters_dict,
    )
    assert filters.apply(value) == expected_result
