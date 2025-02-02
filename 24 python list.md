#  Python List 


## What is a List?

A list is an **ordered collection of items**.

- Python uses square brackets (`[]`) to define a list.
- A list can contain one or more items, separated by commas.

### Example: Empty List

```python
empty_list = []
```
# List of Strings
Lists are often named using plural nouns (e.g., numbers, colors, shopping_carts). Here's an example of defining a list with numbers and strings.

Example: List of Numbers

```python
numbers = [1, 3, 2, 7, 9, 4]
print(numbers)
```
**Output:**

```csharp
[1, 3, 2, 7, 9, 4]
```
# Example: List of Colors 
```python
colors = ['red', 'green', 'blue']
print(colors)
```
**Output:**

```css
['red', 'green', 'blue']
```
# List of Lists (Nested Lists)
A list can also contain other lists (nested lists).

```python
coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)
```
**Output:**

[[0, 0], [100, 100], [200, 200]]

# Accessing Elements in a List
Since a list is ordered, you can access its elements using indexes.

```python
list[index]
```
Lists are zero-based indexed, meaning the first element has an index of 0.
## Example 1: Accessing First Element
```python
numbers = [1, 3, 2, 7, 9, 4]
print(numbers[0])  # Output: 1
```
 ## Example 2: Accessing Second Element
```python
numbers = [1, 3, 2, 7, 9, 4]
print(numbers[1])  # Output: 3
```
## Negative Indexing
You can also use negative indexing to access elements starting from the end of the list.

```python
numbers = [1, 3, 2, 7, 9, 4]
print(numbers[-1])  # Output: 4
print(numbers[-2])  # Output: 9
```
Modifying, Adding, and Removing Elements
## 1. Modifying Elements in a List
You can change an element by assigning a new value using:

```python
list[index] = new_value
```
## Example 1: Modifying the First Element
```python
numbers = [1, 3, 2, 7, 9, 4]
numbers[0] = 10
print(numbers)  # Output: [10, 3, 2, 7, 9, 4]
```
# Example 2: Modifying the Second Element
```python

numbers = [1, 3, 2, 7, 9, 4]
numbers[1] = numbers[1] * 10
print(numbers)  # Output: [1, 30, 2, 7, 9, 4]
```
## 2. Adding Elements to a List
You can use the following methods to add elements:

append(): Adds an element to the end.
insert(): Inserts an element at a specific index.
## Example 1: Using append()
```python
numbers = [1, 3, 2, 7, 9, 4]
numbers.append(100)
print(numbers)  # Output: [1, 3, 2, 7, 9, 4, 100]
```
## Example 2: Using insert()
```python
numbers = [1, 3, 2, 7, 9, 4]
numbers.insert(2, 100)
print(numbers)  # Output: [1, 3, 100, 2, 7, 9, 4]
```
## 3. Removing Elements from a List
You can remove elements in various ways:

**del statement:** Removes an element at a specific index.

**pop():** Removes the last element or an element at a specific index and returns it.

**remove():** Removes the first occurrence of a specific value.

## Example 1: Using del Statement
```python
numbers = [1, 3, 2, 7, 9, 4]
del numbers[0]
print(numbers)  # Output: [3, 2, 7, 9, 4]
```
## Example 2: Using pop()
 ```python
numbers = [1, 3, 2, 7, 9, 4]
last = numbers.pop()
print(last)     # Output: 4
print(numbers)  # Output: [1, 3, 2, 7, 9]
```
## Example 3: Using pop() with Index
```python
numbers = [1, 3, 2, 7, 9, 4]
second = numbers.pop(1)
print(second)    # Output: 3
print(numbers)   # Output: [1, 2, 7, 9, 4]
```
## Example 4: Using remove() by Value
 ```python
numbers = [1, 3, 2, 7, 9, 4, 9]
numbers.remove(9)
print(numbers)  # Output: [1, 3, 2, 7, 4, 9]
```
**Note: The remove() method removes only the first occurrence of the specified value.**

# Summary
A list is an ordered collection of items.

You can access elements using zero-based indexing (list[index]).

Use negative indexing to access elements starting from the end (list[-1]).

To modify an element, use list[index] = new_value.

To add an element, use append() or insert().

To remove an element, use del, pop(), or remove().