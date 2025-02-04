import pytest
from filterutil import Filter, Filters, XorFilters, LogicGate


def test_xor_filters_init():
    filters = XorFilters()
    assert isinstance(filters, Filters)


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
            },
            True,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 2),
            },
            False,
        ),
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
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
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
                'c': Filter(lambda x: isinstance(x, int)),
            },
            False,
        ),
    ],
)
def test_xor_filters_filtering(value, filters_dict, expected_result):
    filters = XorFilters(**filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
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
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
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
    ],
)
def test_xor_filters_update(value, filters_dict, expected_result):
    filters = XorFilters()
    filters.update(filters_dict)
    assert filters.apply(value) == expected_result


@pytest.mark.parametrize(
    'value, filters_dict, expected_result',
    [
        (
            1,
            {
                'a': Filter(lambda x: x == 1),
                'b': Filter(lambda x: isinstance(x, str)),
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
    ],
)
def test_filters_as_xor(value, filters_dict, expected_result):
    filters = Filters(
        LogicGate.XOR,
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
            },
            {
                ('a', 'c'): True,
                ('a', 'b'): False,
                ('b', 'c'): True,
            },
        ),
    ],
)
def test_xor_filters_select(value, filters_dict, expected_result):
    filters = XorFilters(**filters_dict)
    for filter_names, filters_expected_result in expected_result.items():
        assert filters.apply(value, filter_names=filter_names) == filters_expected_result
