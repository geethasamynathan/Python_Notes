# 1. What is a Lambda Function? 
A lambda function in Python is an anonymous function, meaning it doesn't have a name. It is used to create small, single-use functions for short tasks. A lambda function can take any number of arguments but only contains a single expression.
# syntax
`lambda arguments: expression`

lambda is the keyword to define a lambda function.

arguments are the inputs that the function takes (can be zero or more).

expression is the logic that the lambda function evaluates and returns.

## Example:
```python
 
# Simple lambda function that adds 10 to the given number
add_10 = lambda x: x + 10

print(add_10(5))  # Output: 15
```
In this example, the lambda function lambda x: x + 10 takes one argument x and returns x + 10.

# 2. Lambda Function with Multiple Arguments 
Lambda functions can take multiple arguments and perform operations based on them.

Example:
```python
 
# Lambda function with two arguments
multiply = lambda x, y: x * y

print(multiply(4, 5))  # Output: 20
```
In this case, lambda x, y: x * y takes two arguments x and y, and returns their product.


You can use a lambda function to compute the total price of items in a cart where you have multiple quantities and prices.

```python
 
# Lambda function to calculate the total price of two items
calculate_total = lambda price, quantity: price * quantity

total = calculate_total(10, 3)  # Output: 30
print(total)
```
# 3. Lambda Function with Conditional Statements 
You can also use conditional expressions in lambda functions to make decisions.

Syntax:
lambda arguments: value_if_true if condition else value_if_false
Example:
```python
 
# Lambda function with a condition
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(4))  # Output: Even
print(check_even(7))  # Output: Odd
```
In this example, the lambda function checks if a number is even or odd and returns "Even" or "Odd" accordingly.

# 4. Lambda Functions with Built-in Functions 
Lambda functions are commonly used with built-in functions like map(), filter(), and sorted() for functional programming.

# Example 1: Using map()
The map() function applies a function to all items in an input list and returns an iterable map object. You can use lambda functions with map() to perform operations on each item of a list.

```python
 
# Using map() to add 5 to each element in the list
numbers = [1, 2, 3, 4, 5]
result = map(lambda x: x + 5, numbers)

print(list(result))  # Output: [6, 7, 8, 9, 10]
```
In this example, the lambda function lambda x: x + 5 is applied to each item in the numbers list.

# Example 2: Using filter()
The filter() function filters items in a list based on a condition defined by the function. You can use lambda functions with filter() to filter elements that satisfy a condition.

```python
 
# Using filter() to get only numbers greater than 3
numbers = [1, 2, 3, 4, 5]
result = filter(lambda x: x > 3, numbers)

print(list(result))  # Output: [4, 5]
```
In this example, the lambda function filters the numbers that are greater than 3.

# Example 3: Using sorted()
The sorted() function is used to sort an iterable (e.g., list). You can use lambda functions with sorted() to customize the sorting behavior.

```python
 
# Sorting a list of tuples based on the second item (age)
people = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_people = sorted(people, key=lambda person: person[1])

print(sorted_people)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
```
In this example, the lambda function is used as the sorting key to sort the list of tuples by the second item (age).

# 5. Lambda Function for Sorting with Complex Conditions 
You can use lambda functions for more advanced sorting, such as sorting a list of dictionaries or tuples with complex conditions.

Example: Sorting by Multiple Conditions
```python
 
# List of employees with their names and salaries
employees = [
    {"name": "Alice", "salary": 50000},
    {"name": "Bob", "salary": 60000},
    {"name": "Charlie", "salary": 40000}
]

# Sorting by salary, and then by name alphabetically
sorted_employees = sorted(employees, key=lambda x: (x["salary"], x["name"]))

print(sorted_employees)
# Output: [{'name': 'Charlie', 'salary': 40000}, {'name': 'Alice', 'salary': 50000}, {'name': 'Bob', 'salary': 60000}]
```

## Sort by salary (descending) and name (ascending)
```python
sorted_employees = sorted(
    employees, 
    key=lambda x: (-x['salary'], x['name'])
)

print(sorted_employees)
```
## Sort by salary (ascending) and name (descending)
```python
sorted_employees = sorted(
    employees, 
    key=lambda x: (x['salary'], -x['name']) # error negation on string is not applicable
)

print(sorted_employees)
```
# 6. Using Lambda for Inline Function Definition 
Lambda functions are perfect for cases where you need a short, throwaway function that you don’t plan on reusing. This is particularly useful when working with higher-order functions (functions that accept other functions as arguments).

# Example: Using Lambda with reduce()
The reduce() function from the functools module is used to apply a rolling computation to sequential pairs of values in an iterable.

```python 
from functools import reduce

# Using reduce() to multiply all elements in the list
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)

print(product)  # Output: 24
```
In this case, the lambda function lambda x, y: x * y is used to multiply all the numbers in the list numbers.

# 7. Practical Real-World Example of Lambda Functions 
Let’s combine all the concepts into a practical example where we process a list of dictionaries that represent products in a store. We’ll use lambda functions for filtering, sorting, and mapping data.

Example: Processing Product Data
```python
 
products = [
    {"name": "Product A", "price": 200, "category": "Electronics"},
    {"name": "Product B", "price": 50, "category": "Clothing"},
    {"name": "Product C", "price": 150, "category": "Electronics"},
    {"name": "Product D", "price": 300, "category": "Furniture"}
]

# Step 1: Filter products that are in the Electronics category
electronics = filter(lambda p: p["category"] == "Electronics", products)
for item in electronic_items:
    print(item)
# Step 2: Sort the filtered products by price (ascending)
sorted_electronics = sorted(electronics, key=lambda p: p["price"])

# Step 3: Map the products to their names and prices
product_info = map(lambda p: (p["name"], p["price"]), sorted_electronics)

# Print the results
for info in product_info:
    print(info)
Output:
mathematica
 
('Product C', 150)
('Product A', 200)
```
# Summary
**Beginner Level:** Lambda functions are small, anonymous functions used for short tasks. They can take any number of arguments and return the result of a single expression.

**Intermediate Level:** Lambda functions can take multiple arguments and can also include conditional statements. They're often used with functions like map(), filter(), and sorted().

**Advanced Level:** Lambda functions are useful for more complex tasks such as sorting by multiple criteria, applying functions to a sequence of elements (using reduce()), and handling complex conditions in real-world applications.

Lambda functions are powerful tools in python that allow for concise, readable, and efficient code. They are especially useful in functional programming scenarios.