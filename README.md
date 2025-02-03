# filterutil
**filterutil** is simple, yet very powerful filtering tool.

## How to install
You could install from PyPi:
```bash
$ python3 -m pip install filterutil
```

## How to use
### Simple filter
```python
from filterutil import Filter


def test_func():
    my_filter = Filter(lambda x: x == 1)
    # assert False
    assert not my_filter.apply(2):
```

### Coupling filters with AND policy
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 1)
    b = Filter(lambda x: isinstance(x, int))
    compound_filter = a & b
    # order matters:
    #     "compound_filter = a & b" means first a then b
    #     "compound_filter = b & a" means first b then a
    
    # assert False
    assert not compound_filter.apply(2)
```

### Coupling filters with OR policy
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 1)
    b = Filter(lambda x: isinstance(x, int))
    # order still matters
    compound_filter = a | b

    # assert True
    assert compound_filter.apply(2)
```

### Coupling filters with XOR policy
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 1)
    b = Filter(lambda x: x == 3)
    compound_filter = a ^ b

    # assert True
    assert compound_filter.apply(2)
```

### Infinite nesting
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: isinstance(x, int))
    b = Filter(lambda x: isinstance(x, str))
    c = Filter(lambda x: x == 1)
    # multiline
    compound_filter = a | b
    compound_filter = compound_filter & c
    # order is: (a or b) and c
    # assert False
    assert not compound_filter.apply(2)

    # is not the same as inline
    # because of python operator precedence
    compound_filter = filter_a | filter_b & filter_c
    # order is: a or (b and c)
    # assert True
    assert compound_filter.apply(2)
```

### Collection of filters with same policy
```python
from filterutil import Filter, Filters, OrFilters, XorFilters, FilterCouplingPolicy


def test_func():
    # Filters is AND collection by default
    and_filters = Filters()
    and_filters['a'] = Filter(lambda x: isinstance(x, int))
    and_filters['b'] = Filter(lambda x: isinstance(x, str))
    
    # same as
    and_filters = Filters(
        a=Filter(lambda x: isinstance(x, int)),
        b=Filter(lambda x: isinstance(x, str)),
    )
    # ---

    # assert False
    assert not and_filters.apply(2)

    # OR collection
    or_filters = OrFilters()
    
    #same as 
    or_filters = Filters(FilterCouplingPolicy.OR)
    # ---

    or_filters['a'] = Filter(lambda x: isinstance(x, int))
    or_filters['b'] = Filter(lambda x: isinstance(x, str))

    # assert True
    assert or_filters.apply(2)
    
    # XOR collection
    xor_filters = XorFilters()

    #same as 
    xor_filters = Filters(FilterCouplingPolicy.XOR)
    # ---

    xor_filters['a'] = Filter(lambda x: isinstance(x, int))
    xor_filters['b'] = Filter(lambda x: isinstance(x, str))

    # assert True
    assert xor_filters.apply(False)
```

### Infinite nesting of collections
```python
from filterutil import Filter, Filters, OrFilters, XorFilters, FilterCouplingPolicy


def test_func():
    and_filters = Filters(
        FilterCouplingPolicy.AND,
        a=Filter(lambda x: isinstance(x, int)),
        b=Filter(lambda x: isinstance(x, str)),
    )
    xor_filters = Filters(
        FilterCouplingPolicy.XOR,
        a=Filter(lambda x: x == 1),
        b=Filter(lambda x: x == 3),
    )

    two_collections_in_one = OrFilters(
        first=and_filters,
        second=xor_filters,
    )
    # assert True
    assert two_collections_in_one.apply(2)
```
