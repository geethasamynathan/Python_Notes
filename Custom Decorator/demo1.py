import time
import functools

def log_execution(func):
    """A custom decorator to log function calls and execution time."""
    
    @functools.wraps(func)  # Preserves function metadata (name, docstring)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the actual function
        end_time = time.time()  # Record end time
        
        print(f"Function '{func.__name__}' called with arguments: {args}, {kwargs}")
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        
        return result  # Return the original function's result
    
    return wrapper  # Return the modified function
@log_execution
def add_numbers(a, b):
    """Function to add two numbers."""
    time.sleep(1)  # Simulate some processing delay
    return a + b

@log_execution
def prodcut(a, b):
    """Function to add two numbers."""
    time.sleep(1)  # Simulate some processing delay
    add_numbers(34,65)
    return a * b

result = add_numbers(5, 10)
productresult=prodcut(4,5)
print("Result:", result)
print("Result:", productresult)