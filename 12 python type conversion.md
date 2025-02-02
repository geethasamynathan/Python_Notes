# Python Type Conversion

## Introduction to Type Conversion in Python
To get input from users, you use the `input()` function. For example:

```python
value = input('Enter a value:')
print(value)
```

When you execute this code, it’ll prompt you for input on the Terminal:

```
Enter a value:
```

If you enter a value, for example, a number, the program will display that value back:

```
Enter a value: 100
100
```

However, the `input()` function returns a string, not an integer.

The following example prompts you to enter two input values: net price and tax rate. After that, it calculates the tax and displays the result on the screen:

```python
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

tax_amount = price * tax / 100

print(f'The tax amount price is ${tax_amount}')
```

When you execute the program and enter some numbers:

```
Enter the price ($): 100
Enter the tax rate (%): 10
```

You’ll get the following error:

```
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    tax_amount = price * tax / 100
TypeError: can't multiply sequence by non-int of type 'str'
```

Since the input values are strings, you cannot apply the multiply operator.

To solve this issue, you need to convert the strings to numbers before performing calculations.

To convert a string to a number, you use the `int()` function. More precisely, the `int()` function converts a string to an integer.

The following example uses the `int()` function to convert the input strings to numbers:

```python
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

tax_amount = int(price) * int(tax) / 100
print(f'The tax amount is ${tax_amount}')
```

If you run the program, and enter some values, you’ll see that it works correctly:

```
Enter the price ($): 100
Enter the tax rate (%): 10
The tax amount is $10.0
```

## Other Type Conversion Functions
Besides the `int(str)` function, Python supports other type conversion functions. The following shows the most important ones for now:

- `float(str)` – convert a string to a floating-point number.
- `bool(val)` – convert a value to a boolean value, either `True` or `False`.
- `str(val)` – return the string representation of a value.

## Getting the Type of a Value
To get the type of a value, you use the `type(value)` function. For example:

```python
>>> type(100)
<class 'int'>
>>> type(2.0)
<class 'float'>
>>> type('Hello')
<class 'str'>
>>> type(True)
<class 'bool'>
```

As you can see clearly from the output:

- The number `100` has the type of `int`.
- The number `2.0` has the type of `float`.
- The string `'Hello'` has the type of `str`.
- The `True` value has the type of `bool`.

In front of each type, you see the `class` keyword. It isn’t important for now, and you’ll learn more about the `class` later.

## Summary
- Use the `input()` function to get an input string from users.
- Use type conversion functions such as `int()`, `float()`, `bool()`, and `str(value)` to convert a value from one type to another.
- Use the `type()` function to get the type of a value.


### Example 1: Converting String to Integer
**Scenario:** You're building a ticket booking system, and the number of tickets to be booked is entered as a string by the user. You need to convert it to an integer to perform calculations.

```python
# Input
num_tickets = input("Enter the number of tickets: ")

# Type conversion from string to integer
num_tickets = int(num_tickets)

# Calculations
total_cost = num_tickets * 150
print(f"The total cost for {num_tickets} tickets is {total_cost} INR.")
```
## Example 2: Converting String to Float
Scenario: You're developing a financial application where the user inputs the interest rate as a string. You need to convert it to a float to perform interest calculations.
```python
# Input
interest_rate = input("Enter the interest rate: ")

# Type conversion from string to float
interest_rate = float(interest_rate)

# Calculations
principal = 10000
interest = principal * (interest_rate / 100)
print(f"The interest on the principal amount at a rate of {interest_rate}% is {interest} INR.")
```
## Example 3: Converting Integer to String
Scenario: You're creating a user profile display where you need to show the user's age as part of a string message.
```python
# Input
age = 25

# Type conversion from integer to string
age_str = str(age)

# Displaying the message
print("The user's age is " + age_str + " years.")

```

## Example 4: Converting List to Tuple
Scenario: You're working on a project where you need to ensure the elements of a list are immutable, so you convert the list to a tuple.

```python
# Input
fruits_list = ["apple", "banana", "cherry"]

# Type conversion from list to tuple
fruits_tuple = tuple(fruits_list)

print(f"The fruits are: {fruits_tuple}")
```

## Example 5: Converting Dictionary Keys to List
Scenario: You're processing user data stored in a dictionary and need to extract all the user IDs as a list.
```python
# Input
user_data = {"user1": "Alice", "user2": "Bob", "user3": "Charlie"}

# Type conversion from dictionary keys to list
user_ids = list(user_data.keys())

print(f"The user IDs are: {user_ids}")

```