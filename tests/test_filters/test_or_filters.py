import pytest
from filterutil import Filter, Filters, OrFilters, LogicGate


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
        LogicGate.OR,
        **filters_dict,
    )
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 2), 
                'b': Filter(lambda x: isinstance(x, int)),
                'c': Filter(lambda x: isinstance(x, str)),
            },
            {
                ('a', 'b'): True,
                ('a', 'c'): False,
            },
        ),
    ],
)
def test_or_filters_select(value, filters_dict, expected_result):
    filters = OrFilters(**filters_dict)
    for filter_names, filters_expected_result in expected_result.items():
        assert filters.apply(value, filter_names=filter_names) == filters_expected_result
