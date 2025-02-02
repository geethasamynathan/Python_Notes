
# Python Logical Operators

## Introduction to Python Logical Operators
Sometimes, you may want to check multiple conditions at the same time. To do so, you use logical operators.

Python has three logical operators:
- **and**
- **or**
- **not**

## The `and` Operator
The **and** operator checks whether two conditions are both `True` simultaneously:

```python
a and b
```

It returns `True` if both conditions are `True`, and it returns `False` if either the condition `a` or `b` is `False`.

The following example uses the **and** operator to combine two conditions that compare the price with numbers:

```python
>>> price = 9.99
>>> price > 9 and price < 10
True
```

The result is `True` because the price is greater than 9 and less than 10.

The following example returns `False` because the price isn’t greater than 10:

```python
>>> price > 10 and price < 20
False
```

In this example, the condition `price > 10` returns `False`, while the second condition `price < 20` returns `True`.

The following table illustrates the result of the **and** operator when combining two conditions:

| a     | b     | a and b |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | False   |
| False | False | False   |
| False | True  | False   |

As you can see from the table, the condition `a and b` only returns `True` if both conditions evaluate to `True`.

## The `or` Operator
Similar to the **and** operator, the **or** operator checks multiple conditions. But it returns `True` when either or both individual conditions are `True`:

```python
a or b
```

The following table illustrates the result of the **or** operator when combining two conditions:

| a     | b     | a or b |
|-------|-------|--------|
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

The **or** operator returns `False` only when both conditions are `False`.

The following example shows how to use the **or** operator:

```python
>>> price = 9.99
>>> price > 10 or price < 20
True
```

In this example, the `price < 20` condition returns `True`, so the whole expression returns `True`.

The following example returns `False` because both conditions evaluate to `False`:

```python
>>> price = 9.99
>>> price > 10 or price < 5
False
```

## The `not` Operator
The **not** operator applies to one condition and reverses the result of that condition. If the condition is `True`, the **not** operator returns `False`, and vice versa:

```python
not a
```

The following table illustrates the result of the **not** operator:

| a     | not a |
|-------|-------|
| True  | False |
| False | True  |

The following example uses the **not** operator. Since `price > 10` returns `False`, `not price > 10` returns `True`:

```python
>>> price = 9.99
>>> not price > 10
True
```

Here is another example that combines the **not** and the **and** operators:

```python
>>> not (price > 5 and price < 10)
False
```

In this example, Python evaluates the conditions in the following order:
1. `(price > 5 and price < 10)` evaluates to `True`.
2. `not True` evaluates to `False`.

## Precedence of Logical Operators
When you mix logical operators in an expression, Python evaluates them based on the **precedence of logical operators**.

The following shows the precedence of the `not`, `and`, and `or` operators:

| Operator | Precedence |
|----------|------------|
| not      | High       |
| and      | Medium     |
| or       | Low        |

Based on these precedences, Python groups operands for the operator with the highest precedence first, then groups operands for the operator with the lower precedence, and so on.

If an expression has several logical operators with the same precedence, Python evaluates them from left to right:

```python
a or b and c    means    a or (b and c)
a and b or c and d    means    (a and b) or (c and d)
a and b and c or d    means    ((a and b) and c) or d
not a and b or c    means    ((not a) and b) or c
```

## Summary
- Use logical operators to combine multiple conditions.
- Python has three logical operators: `and`, `or`, and `not`.
- The precedence of the logical operators from highest to lowest is: `not`, `and`, and `or`.
