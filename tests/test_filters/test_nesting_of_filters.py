import pytest
from filterutil import Filter, Filters, OrFilters


@pytest.mark.parametrize(
    'value, first_collection, second_collection, final_collection_class, expected_result',
    [
        (
            2,
            Filters(
                a=Filter(lambda x: isinstance(x, int)),
                b=Filter(lambda x: isinstance(x, str)),
            ),
            OrFilters(
                a=Filter(lambda x: x == 1),
                b=Filter(lambda x: bool(x)),
            ),
            OrFilters,
            True,
        )
    ],
)
def test_nesting_of_collections(
    value,
    first_collection,
    second_collection,
    final_collection_class,
    expected_result,
):
    two_collections_in_one = final_collection_class(
        first=first_collection,
        second=second_collection,
    )
    assert two_collections_in_one.apply(value) == expected_result
