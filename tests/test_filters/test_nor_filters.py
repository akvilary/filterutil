import pytest
from filterutil import Filter, Filters, NorFilters, LogicGate


def test_nor_filters_init():
    filters = NorFilters()
    assert isinstance(filters, Filters)


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, int)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
                'c': Filter(lambda x: x is None),
            },
            False,
        ),
    ],
)
def test_nor_filters_filtering(value, filters_dict, expected_result):
    filters = NorFilters(**filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, int)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
                'c': Filter(lambda x: x is None),
            },
            False,
        ),
    ],
)
def test_nor_filters_setitem(value, filters_dict, expected_result):
    filters = NorFilters()
    for k, v in filters_dict.items():
        filters[k] = v
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, int)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
                'c': Filter(lambda x: x is None),
            },
            False,
        ),
    ],
)
def test_nor_filters_update(value, filters_dict, expected_result):
    filters = NorFilters()
    filters.update(filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, int)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
                'c': Filter(lambda x: x is None),
            },
            False,
        ),
    ],
)
def test_filters_as_nor(value, filters_dict, expected_result):
    filters = Filters(
        LogicGate.NOR,
        **filters_dict,
    )
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
                'd': Filter(lambda x: x is None),
            },
            {
                ('a', 'b'): False,
                ('a', 'c'): False,
                ('c', 'd'): True,
            },
        ),
    ],
)
def test_nor_filters_select(value, filters_dict, expected_result):
    filters = NorFilters(**filters_dict)
    for filter_names, filters_expected_result in expected_result.items():
        assert filters.apply(value, filter_names=filter_names) == filters_expected_result
