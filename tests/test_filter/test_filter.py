from filterutil import Filter


def test_filter_init():
    filter_a = Filter(lambda x: x == 1)
    assert isinstance(filter_a, Filter)
