# Python Boolean

## Introduction to Python Boolean Data Type

In programming, you often want to check if a condition is true or not and perform some actions based on the result.

To represent true and false, Python provides you with the boolean data type. The boolean value has a technical name as `bool`.

The boolean data type has two values: `True` and `False`.

Note that the boolean values `True` and `False` start with the capital letters `(T)` and `(F)`.

The following example defines two boolean variables:

```python
is_active = True
is_admin = False
```

# Comparing Values

When you compare two numbers, Python returns the result as a boolean value. For example:

```python
>>> 20 > 10
True
>>> 20 < 10
False
```

Also, comparing two strings results in a boolean value:

```python
>>> 'a' < 'b'
True
>>> 'a' > 'b'
False
```

# The `bool()` Function

To find out if a value is `True` or `False`, you use the `bool()` function. For example:

```python
>>> bool('Hi')
True
>>> bool('')
False
>>> bool(100)
True
>>> bool(0)
False
```

As you can see clearly from the output, some values evaluate to `True` and the others evaluate to `False`.

# Falsy and Truthy Values

When a value evaluates to `True`, it’s *truthy*. And if a value evaluates to `False`, it’s *falsy*.

### Falsy Values

The following are falsy values in Python:

- The number zero (`0`)
- An empty string (`''`)
- `False`
- `None`
- An empty list (`[]`)
- An empty tuple (`()`)
- An empty dictionary (`{}`)

### Truthy Values

The truthy values are the other values that aren’t falsy.

Note that you’ll learn more about the `None`, `list`, `tuple`, and `dictionary` in the upcoming sessions.

# Summary

- Python boolean data type has two values: `True` and `False`.
- Use the `bool()` function to test if a value is `True` or `False`.
- The falsy values evaluate to `False`, while the truthy values evaluate to `True`.
- Falsy values are the number zero, an empty string, `False`, `None`, an empty list, an empty tuple, and an empty dictionary. Truthy values are the values that are not falsy.
