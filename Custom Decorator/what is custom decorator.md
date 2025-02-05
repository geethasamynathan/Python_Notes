# Custom Decorators in Python

## What is a Custom Decorator?
A **custom decorator** in Python is a function that **modifies the behavior** of another function **without changing its code**. It is commonly used for:
- **Logging** function calls
- **Authentication** and security
- **Performance measurement**
- **Caching** to improve efficiency

---

## When to Use Custom Decorators?
Use custom decorators when you need to:
1. **Reuse functionality** without modifying existing functions.
2. **Add pre-processing or post-processing** (e.g., logging, timing).
3. **Enforce security/authentication** in APIs or web applications.
4. **Implement caching mechanisms** to speed up repeated function calls.

---

## Real-World Example: Logging Function Calls

### Step 1: Define the Custom Decorator
```python
import time  # Import time module for execution time measurement
import functools  # Import functools to preserve function metadata

def log_execution(func):  # Define a decorator that takes a function as input
    """A custom decorator to log function calls and execution time."""
    
    @functools.wraps(func)  # Preserves function metadata (name, docstring)
    def wrapper(*args, **kwargs):  # Define an inner function to modify behavior
        start_time = time.time()  # Record the start time before executing the function
        result = func(*args, **kwargs)  # Call the actual function with its arguments
        end_time = time.time()  # Record the end time after function execution
        
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result  # Return the original function's result
    
    return wrapper  # Return the modified function
```
# Explanation:
**def log_execution(func):** → Accepts a function and modifies its behavior.
**@functools.wraps(func)** → Preserves the function name and docstring.
**def wrapper(*args, **kwargs):** → Calls the function while logging execution time.
**time.time()** → Records execution start and end time.
Prints function name, arguments, and execution time.
Returns the result of the actual function.

# Step 2: Apply the Decorator to a Function

```python
@log_execution  # Apply the decorator
def add_numbers(a, b):
    """Function to add two numbers."""
    time.sleep(1)  # Simulate some processing delay
    return a + b
```

# Explanation:
**@log_execution** → Applies the decorator before the function.
When add_numbers(5, 10) is called, log_execution will modify its behavior.
**time.sleep(1)** → Simulates a delay to measure execution time.

# Step 3: Call the Function and Observe the Logs

```python
result = add_numbers(5, 10)
print("Result:", result)

```

# More Real-World Use Cases
1. Authentication Check in Web Apps
```python
def require_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.get('is_authenticated', False):  # Check if user is authenticated
            raise PermissionError("User is not authenticated!")
        return func(user, *args, **kwargs)  # Call the actual function
    return wrapper  # Return the modified function

@require_authentication
def view_profile(user):
    return f"Welcome {user['name']}!"

# Simulating a user
user = {'name': 'John Doe', 'is_authenticated': True}
print(view_profile(user))  # ✅ Works fine

user_not_authenticated = {'name': 'Jane Doe', 'is_authenticated': False}
print(view_profile(user_not_authenticated))  # ❌ Raises PermissionError
```
## Explanation:
The decorator checks if the user is authenticated.
If not authenticated, it raises a PermissionError.
Otherwise, it executes the function normally.


# 2. Caching Function Results
```python

cache = {}  # Dictionary to store computed values

def memoize(func):
    def wrapper(n):
        if n in cache:  # Check if result is already in cache
            print("Fetching from cache...")
            return cache[n]
        result = func(n)  # Compute the result
        cache[n] = result  # Store in cache
        return result
    return wrapper

@memoize
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))  # Computes and stores result
print(factorial(5))  # Fetches from cache
```
## Explanation:
Stores function results in a dictionary.
Avoids redundant computations for repeated inputs.

### Summary
Custom decorators modify function behavior without modifying actual code.

Use Cases: Logging, Authentication, Performance Monitoring, Caching, etc.

Implemented with @decorator_name before a function definition.
Uses functools.wraps(func) to retain function metadata.