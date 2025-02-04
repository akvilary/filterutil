import pytest
from filterutil import Filter, CompoundFilter


@pytest.mark.parametrize(
    'value, filters, expected_result',
    [
        (1, [Filter(lambda x: x == 1), Filter(lambda x: isinstance(x, str))], True),
        (1, [Filter(lambda x: x == 2), Filter(lambda x: isinstance(x, str))], True),
        (1, [Filter(lambda x: x == 1), Filter(lambda x: isinstance(x, int))], False),
    ],
)
def test_nand_filters(value, filters, expected_result):
    compound_filter = None
    for _filter in filters:
        if compound_filter is None:
            compound_filter = _filter
        else:
            compound_filter = compound_filter.nand(_filter)
    assert isinstance(compound_filter, CompoundFilter)
    result = compound_filter.apply(value)
    assert result == expected_result
