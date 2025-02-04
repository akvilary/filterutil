import pytest
from filterutil import Filter, Filters, LogicGate


def test_filters_init():
    filters = Filters()
    assert isinstance(filters, Filters)
    assert filters.default_logic_gate == LogicGate.AND


def test_filters_init_with_none():
    filters = Filters(None)
    assert isinstance(filters, Filters)
    assert filters.default_logic_gate == LogicGate.AND


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

@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1), 
                'b': Filter(lambda x: isinstance(x, int)),
                'c': Filter(lambda x: isinstance(x, str)),
            },
            {
                ('a', 'b'): True,
                ('b', 'c'): False,
            },
        ),
    ],
)
def test_filters_select(value, filters_dict, expected_result):
    filters = Filters(**filters_dict)
    for filter_names, filters_expected_result in expected_result.items():
        assert filters.apply(value, filter_names=filter_names) == filters_expected_result
