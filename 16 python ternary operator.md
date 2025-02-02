
# Python Ternary Operator


## Introduction to Python Ternary Operator
The following program prompts you for your age and determines the ticket price based on it:

```python
age = input('Enter your age:')

if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5

print(f"The ticket price is {ticket_price}")
```

### Output:
```text
Enter your age: 18
The ticket price is $20
```

In this example, the following `if...else` statement assigns 20 to `ticket_price` if the age is greater than or equal to 18. Otherwise, it assigns the `ticket_price` 5:

```python
if int(age) >= 18:
    ticket_price = 20
else:
    ticket_price = 5
```

To make it more concise, you can use an alternative syntax like this:

```python
ticket_price = 20 if int(age) >= 18 else 5
```

In this statement:
- The left side of the assignment operator (`=`) is the variable `ticket_price`.
- The expression on the right side returns `20` if the age is greater than or equal to 18 or `5` otherwise.

### Ternary Operator Syntax:
```python
value_if_true if condition else value_if_false
```

The ternary operator evaluates the condition. If the result is `True`, it returns `value_if_true`. Otherwise, it returns `value_if_false`.

The ternary operator is equivalent to the following `if...else` statement:

```python
if condition:
    value_if_true
else:
    value_if_false
```

Note: If you're familiar with programming languages such as C# or Java, you might know the following ternary operator syntax:

```python
condition ? value_if_true : value_if_false
```

However, Python does not support this ternary operator syntax.

### Example Using Ternary Operator:
```python
age = input('Enter your age:')

ticket_price = 20 if int(age) >= 18 else 5

print(f"The ticket price is {ticket_price}")
```

## Summary
- The Python ternary operator syntax is:  
  `value_if_true if condition else value_if_false`
- Use the ternary operator to make your code more concise.
