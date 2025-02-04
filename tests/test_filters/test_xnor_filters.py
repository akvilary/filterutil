import pytest
from filterutil import Filter, Filters, XnorFilters, LogicGate


def test_xnor_filters_init():
    filters = XnorFilters()
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
                'b': Filter(lambda x: isinstance(x, int)),
            },
            True,
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
            True,
        ),
    ],
)
def test_xnor_filters_filtering(value, filters_dict, expected_result):
    filters = XnorFilters(**filters_dict)
    assert filters.apply(value) == expected_result


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
                'b': Filter(lambda x: isinstance(x, int)),
            },
            True,
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
            True,
        ),
    ],
)
def test_xnor_filters_setitem(value, filters_dict, expected_result):
    filters = XnorFilters()
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
                'b': Filter(lambda x: isinstance(x, int)),
            },
            True,
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
            True,
        ),
    ],
)
def test_xnor_filters_update(value, filters_dict, expected_result):
    filters = XnorFilters()
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
                'b': Filter(lambda x: isinstance(x, int)),
            },
            True,
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
            True,
        ),
    ],
)
def test_filters_as_xnor(value, filters_dict, expected_result):
    filters = Filters(
        LogicGate.XNOR,
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
                ('a', 'b'): True,
                ('a', 'c'): False,
                ('c', 'd'): True,
            },
        ),
    ],
)
def test_xnor_filters_select(value, filters_dict, expected_result):
    filters = XnorFilters(**filters_dict)
    for filter_names, filters_expected_result in expected_result.items():
        assert filters.apply(value, filter_names=filter_names) == filters_expected_result
