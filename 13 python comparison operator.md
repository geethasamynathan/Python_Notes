
# Python Comparison Operators

## Introduction to Python Comparison Operators
In programming, you often want to compare a value with another value. To do that, you use comparison operators.

Python has six comparison operators, which are as follows:

- **Less than** (`<`)
- **Less than or equal to** (`<=`)
- **Greater than** (`>`)
- **Greater than or equal to** (`>=`)
- **Equal to** (`==`)
- **Not equal to** (`!=`)

These comparison operators compare two values and return a boolean value, either `True` or `False`.

You can use these comparison operators to compare both numbers and strings.

## Less Than Operator (`<`)
The **Less Than** operator (`<`) compares two values and returns `True` if the value on the left is less than the value on the right. Otherwise, it returns `False`:

```python
left_value  < right_value
```

The following example uses the **Less Than** (`<`) operator to compare two numbers:

```python
>>> 10 < 20
True
>>> 30 < 20
False
```

The following example shows how to use the less-than operator (`<`) to compare two strings:

```python
>>> 'apple' < 'orange'
True
>>> 'banana' < 'apple'
False
```

The expression `'apple' < 'orange'` returns `True` because the letter `a` in apple comes before the letter `o` in orange. Similarly, `'banana' < 'apple'` returns `False` because the letter `b` is after the letter `a`.

The following example shows how to use the less-than operator with variables:

```python
>>> x = 10
>>> y = 20
>>> x < y
True
>>> y < x
False
```

## Less Than or Equal To Operator (`<=`)
The **Less Than or Equal To** operator compares two values and returns `True` if the left value is less than or equal to the right value. Otherwise, it returns `False`:

```python
left_value <= right_value
```

The following example shows how to use the less-than or equal to operator to compare two numbers:

```python
>>> 20 <= 20
True
>>> 10 <= 20
True
>>> 30 <= 30
True
```

This example shows how to use the less than or equal to operator to compare the values of two variables:

```python
>>> x = 10
>>> y = 20
>>> x <= y
True
>>> y <= x
False
```

## Greater Than Operator (`>`)
The **Greater Than** operator (`>`) compares two values and returns `True` if the left value is greater than the right value. Otherwise, it returns `False`:

```python
left_value > right_value
```

This example uses the **Greater Than** operator (`>`) to compare two numbers:

```python
>>> 20 > 10
True
>>> 20 > 20
False
>>> 10 > 20
False
```

The following example uses the greater-than operator (`>`) to compare two strings:

```python
>>> 'apple' > 'orange'
False
>>> 'orange' > 'apple'
True
```

## Greater Than or Equal To Operator (`>=`)
The **Greater Than or Equal To** operator (`>=`) compares two values and returns `True` if the left value is greater than or equal to the right value. Otherwise, it returns `False`:

```python
left_value >= right_value
```

The following example uses the greater-than or equal to operator to compare two numbers:

```python
>>> 20 >= 10
True
>>> 20 >= 20
True
>>> 10 >= 20
False
```

The following example uses the greater-than or equal to operator to compare two strings:

```python
>>> 'apple' >= 'apple'
True
>>> 'apple' >= 'orange'
False
>>> 'orange' >= 'apple'
True
```

## Equal To Operator (`==`)
The **Equal To** operator (`==`) compares two values and returns `True` if the left value is equal to the right value. Otherwise, it returns `False`:

```python
left_value == right_value
```

The following example uses the equal to operator (`==`) to compare two numbers:

```python
>>> 20 == 10
False
>>> 20 == 20
True
```

And the following example uses the equal to operator (`==`) to compare two strings:

```python
>>> 'apple' == 'apple'
True
>>> 'apple' == 'orange'
False
```

## Not Equal To Operator (`!=`)
The **Not Equal To** operator (`!=`) compares two values and returns `True` if the left value isn’t equal to the right value. Otherwise, it returns `False`:

```python
left_value != right_value
```

For example, the following uses the not equal to operator to compare two numbers:

```python
>>> 20 != 20
False
>>> 20 != 10
True
```

The following example uses the not equal to operator to compare two strings:

```python
>>> 'apple' != 'apple'
False
>>> 'apple' != 'orange'
True
```

## Summary
- A **comparison operator** compares two values and returns a boolean value, either `True` or `False`.
- Python has six comparison operators: 
  - **Less than** (`<`)
  - **Less than or equal to** (`<=`)
  - **Greater than** (`>`)
  - **Greater than or equal to** (`>=`)
  - **Equal to** (`==`)
  - **Not equal to** (`!=`)
