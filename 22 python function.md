# Python Functions: Basic to Advanced Examples

## 1. Simple Function (Basic Level)

In this example, a function simply prints a message. This represents a basic Python function with no parameters or return values.

**Real-world Scenario:** A program that logs a greeting message to the user.

```python
# Basic function without parameters
def greet():
    print("Hello! Welcome to the program.")

# Calling the function
greet()  # Output: Hello! Welcome to the program.
```
# 2. Function with Parameters (Intermediate Level)
In this example, the function takes parameters to perform a specific task. Here we define a function that takes a person's name and age and returns a greeting with the age.
```python
# Function with parameters
def greet_person(name, age):
    print(f"Hello, {name}! You are {age} years old.")

# Calling the function with arguments
greet_person("Alice", 30)  # Output: Hello, Alice! You are 30 years old.
greet_person("Bob", 25)    # Output: Hello, Bob! You are 25 years old.

```
# 3. Function with Default Parameters 
In this example, a function is defined with default parameter values. If a user does not provide an argument for the parameter, the default value is used.

 A function that logs messages but can default to a specific log level if not provided (e.g., "INFO").

 ```python
# Function with default parameter
def log_message(message, level="INFO"):
    print(f"[{level}] {message}")

# Calling the function
log_message("System startup")  # Output: [INFO] System startup
log_message("Warning: Low memory", "WARNING")  # Output: [WARNING] Warning: Low memory

 ```

 # 4. Function with Multiple Parameters and Default Values
 This example combines both multiple parameters and default values. The function calculates the total price of items, allowing for a discount that defaults to 0 if not provided.

 A shopping cart where customers get a discount (optional) on their total.

 ```python
# Function with multiple parameters and default value
def calculate_total_price(price_per_item, quantity, discount=0):
    total = price_per_item * quantity
    total_after_discount = total - (total * discount / 100)
    return total_after_discount

# Calling the function with and without discount
total = calculate_total_price(100, 5)  # No discount
print(f"Total price without discount: {total}")  # Output: Total price without discount: 500

total_with_discount = calculate_total_price(100, 5, 10)  # With 10% discount
print(f"Total price with discount: {total_with_discount}")  # Output: Total price with discount: 450

 ```
 # 5. Lambda Function (Advanced Level)
Lambda functions are anonymous functions that can take any number of arguments but can only have one expression. They are useful for short operations or when a function is required temporarily.

A filtering system to sort or filter items based on specific conditions (e.g., a list of prices, and you want to find the prices that are above a certain threshold).

```python
# Lambda function for filtering a list of prices
prices = [50, 150, 200, 25, 300, 80]

# Filtering prices greater than 100 using lambda
filtered_prices = list(filter(lambda price: price > 100, prices))
print(filtered_prices)  # Output: [150, 200, 300]

# Lambda function for sorting prices in ascending order
sorted_prices = sorted(prices, key=lambda price: price)
print(sorted_prices)  # Output: [25, 50, 80, 150, 200, 300]

```

# 6. Lambda Function for Complex Real-World Scenario 
In this scenario, the lambda function is used to sort a list of dictionaries based on a specific key, which is a common task when dealing with data in real-world applications.

**Example** : A system that sorts employees by their salary, where each employee is represented by a dictionary containing name and salary information.

```python

# List of employee data
employees = [
    {"name": "Alice", "salary": 60000},
    {"name": "Bob", "salary": 50000},
    {"name": "Charlie", "salary": 70000},
]

# Sorting employees by salary using lambda function
sorted_employees = sorted(employees, key=lambda employee: employee['salary'])

print(sorted_employees)
# Output: [{'name': 'Bob', 'salary': 50000}, {'name': 'Alice', 'salary': 60000}, {'name': 'Charlie', 'salary': 70000}]
```