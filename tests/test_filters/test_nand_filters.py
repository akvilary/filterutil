import pytest
from filterutil import Filter, Filters, NandFilters, LogicGate


def test_nand_filters_init():
    filters = NandFilters()
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
            True,
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
def test_nand_filters_filtering(value, filters_dict, expected_result):
    filters = NandFilters(**filters_dict)
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
            True,
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
def test_nand_filters_setitem(value, filters_dict, expected_result):
    filters = NandFilters()
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
            True,
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
def test_nand_filters_update(value, filters_dict, expected_result):
    filters = NandFilters()
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
            True,
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
def test_filters_as_nand(value, filters_dict, expected_result):
    filters = Filters(
        LogicGate.NAND,
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
                ('a', 'c'): True,
                ('c', 'd'): True,
            },
        ),
    ],
)
def test_nand_filters_select(value, filters_dict, expected_result):
    filters = NandFilters(**filters_dict)
    for filter_names, filters_expected_result in expected_result.items():
        assert filters.apply(value, filter_names=filter_names) == filters_expected_result
