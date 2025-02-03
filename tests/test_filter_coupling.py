import pytest
from filterutil import Filter, CompoundFilter


@pytest.mark.parametrize(
    'value, filters, expected_result',
    [
        (1, [Filter(lambda x: x == 1), Filter(lambda x: isinstance(x, int))], True),
        (1, [Filter(lambda x: x == 1), Filter(lambda x: isinstance(x, str))], False),
    ],
)
def test_add_filters(value, filters, expected_result):
    compound_filter = None
    for _filter in filters:
        if compound_filter is None:
            compound_filter = _filter
        else:
            compound_filter = compound_filter & _filter
    assert isinstance(compound_filter, CompoundFilter)
    result = compound_filter.apply(value)
    assert result == expected_result


@pytest.mark.parametrize(
    'value, filters, expected_result',
    [
        ('A', [Filter(lambda x: x == 1), Filter(lambda x: isinstance(x, str))], True),
        ('A', [Filter(lambda x: x == 1), Filter(lambda x: isinstance(x, int))], False),
    ],
)
def test_or_filters(value, filters, expected_result):
    compound_filter = None
    for _filter in filters:
        if compound_filter is None:
            compound_filter = _filter
        else:
            compound_filter = compound_filter | _filter
    assert isinstance(compound_filter, CompoundFilter)
    result = compound_filter.apply(value)
    assert result == expected_result


@pytest.mark.parametrize(
    'value, first_validator, second_validator, third_validator, expected_result',
    [
        (1, lambda x: x == 'A', lambda x: isinstance(x, str), lambda x: x == 1, True),
        (1, lambda x: x == 1, lambda x: isinstance(x, str), lambda x: x == 'A', True),
        (1, lambda x: x == 'A', lambda x: isinstance(x, str), lambda x: x is None, False),
    ],
)
def test_multi_or_filters(
    value,
    first_validator,
    second_validator,
    third_validator,
    expected_result,
):
    first_filter = Filter(first_validator)
    second_filter = Filter(second_validator)
    third_filter = Filter(third_validator)
    compound_filter = first_filter | second_filter | third_filter
    assert isinstance(compound_filter, CompoundFilter)
    assert isinstance(compound_filter[0], CompoundFilter)
    assert isinstance(compound_filter[1], Filter)
    result = compound_filter.apply(value)
    assert result == expected_result


@pytest.mark.parametrize(
    'value, compound_filters, expected_result',
    [
        (
            1,
            [
                CompoundFilter([Filter(lambda x: x == 'A')]),
                CompoundFilter([Filter(lambda x: isinstance(x, int))]),
            ],
            True,
        ),
        (
            1,
            [
                CompoundFilter([Filter(lambda x: x == 'A')]),
                CompoundFilter([Filter(lambda x: isinstance(x, str))]),
            ],
            False,
        ),
    ],
)
def test_or_compoundfilters(
    value,
    compound_filters,
    expected_result,
):
    compound_filter = None
    for _filter in compound_filters:
        if compound_filter is None:
            compound_filter = _filter
        else:
            compound_filter = compound_filter | _filter

    assert isinstance(compound_filter, CompoundFilter)
    for _filter in compound_filter:
        assert isinstance(_filter, CompoundFilter)

    result = compound_filter.apply(value)
    assert result == expected_result


def test_inline_operator_precedence():
    """
    Check operator precedence
    """
    filter_a = Filter(lambda x: isinstance(x, int))
    filter_b = Filter(lambda x: isinstance(x, str))
    filter_c = Filter(lambda x: x == 1)
    # test multiline
    compound_filter = filter_a | filter_b
    compound_filter = compound_filter & filter_c
    assert not compound_filter.apply(2)

    # test inline
    compound_filter = filter_a | filter_b & filter_c
    assert compound_filter.apply(2)
