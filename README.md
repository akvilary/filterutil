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

### Filter with saved args and kwargs
```python
from typing import Set
from filterutil import Filter


def filtering_func(value: int, y: int):
    return value == y


def test_func():
    # saved args works
    my_filter = Filter(filtering_func, 1)
    # but we recommend to use kwargs
    my_filter = Filter(filtering_func, y=1)

    # assert False
    assert not my_filter.apply(2):
    # .apply under the hood works as
    assert not filtering_func(2, y=1)

    # assert True
    assert my_filter.apply(1):
```

### Coupling filters with AND logic gate
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

### Coupling filters with OR logic gate
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

### Coupling filters with XOR logic gate
True if exactly one input is True.
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 2)
    b = Filter(lambda x: isintance(x, int))
    compound_filter = a ^ b

    # assert True
    assert compound_filter.apply(1)
    # assert False
    assert not compound_filter.apply(2)
```

### Coupling filters with XNOR logic gate
True if both inputs are the same.
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 2)
    b = Filter(lambda x: isintance(x, str))
    compound_filter = a.xnor(b)

    # assert True
    assert compound_filter.apply(1)
```

### Coupling filters with NOR logic gate
True only if all inputs are False.
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 2)
    b = Filter(lambda x: isintance(x, str))
    compound_filter = a.nor(b)

    # assert True
    assert compound_filter.apply(1)
```

### Coupling filters with NAND logic gate
False only if all inputs are True.
```python
from filterutil import Filter


def test_func():
    a = Filter(lambda x: x == 1)
    b = Filter(lambda x: isintance(x, int))
    compound_filter = a.nand(b)

    # assert False
    assert not compound_filter.apply(1)
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

### Collection of filters with same logic gate
```python
from filterutil import (
    Filter,
    Filters,
    OrFilters,
    XorFilters,
    XnorFilters,
    NandFilters,
    NorFilters,
    LogicGate,
)


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
    or_filters = Filters(LogicGate.OR)
    # ---

    or_filters['a'] = Filter(lambda x: isinstance(x, int))
    or_filters['b'] = Filter(lambda x: isinstance(x, str))

    # assert True
    assert or_filters.apply(2)
    
    # XOR collection
    xor_filters = XorFilters()

    #same as 
    xor_filters = Filters(LogicGate.XOR)
    # ---

    xor_filters['a'] = Filter(lambda x: isinstance(x, bool))
    xor_filters['b'] = Filter(lambda x: isinstance(x, str))

    # assert True
    assert xor_filters.apply(False)

    # another logic collections
    xnor_filters = XnorFilters()
    nor_filters = NorFilters()
    nand_filters = NandFilters()
```

### Supported logic gates
```python
from enum import StrEnum


class LogicGate(StrEnum):
    """
    Enum of logic gate
    """
    AND = 'and'
    OR = 'or'
    XOR = 'xor'
    XNOR = 'xnor'
    NAND = 'nand'
    NOR = 'nor'
```

### It is possible to select certain filters of collection
```python
from filterutil import Filter, Filters, OrFilters


def test_func():
    and_filters = Filters(
        a=Filter(lambda x: x == 2), 
        b=Filter(lambda x: isinstance(x, int)),
        c=Filter(lambda x: isinstance(x, str)),
    )
    assert and_filters.apply(2, filter_names=['a', 'b'])
    assert not and_filters.apply(2, filter_names=['b', 'c'])

    or_filters = OrFilters(
        a=Filter(lambda x: x == 1), 
        b=Filter(lambda x: isinstance(x, int)),
        c=Filter(lambda x: isinstance(x, str)),
    )
    assert or_filters.apply(2, filter_names=['a', 'b'])
    assert not or_filters.apply(2, filter_names=['a', 'c'])
```

### Apply another logic gate for the collection dinamically
```python
from filterutil import Filter, Filters, OrFilters, LogicGate


def test_func():
    and_filters = Filters(
        a=Filter(lambda x: x == 1), 
        b=Filter(lambda x: isinstance(x, int)),
    )
    assert not and_filters.apply(2)
    assert and_filters.apply_or(2)
    # or
    assert and_filters.apply(2, logic_gate=LogicGate.OR)


    or_filters = OrFilters(
        a=Filter(lambda x: x == 1), 
        b=Filter(lambda x: isinstance(x, int)),
    )
    assert or_filters.apply(2)
    assert or_filters.apply_xor(2)
    assert not or_filters.apply_and(2)
```

### Infinite nesting of collections
```python
from filterutil import Filter, Filters, OrFilters, XorFilters, LogicGate


def test_func():
    and_filters = Filters(
        LogicGate.AND,
        a=Filter(lambda x: isinstance(x, int)),
        b=Filter(lambda x: isinstance(x, str)),
    )
    xor_filters = Filters(
        LogicGate.XOR,
        a=Filter(lambda x: x == 1),
        b=Filter(lambda x: isintance(x, int)),
    )

    two_collections_in_one = OrFilters(
        first=and_filters,
        second=xor_filters,
    )
    # assert True
    assert two_collections_in_one.apply(2)
```
