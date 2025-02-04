from filterutil import Filter


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
