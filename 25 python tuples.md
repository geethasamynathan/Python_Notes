# Introduction to Python Tuples

Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.

A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.

## Defining a Tuple

A tuple is like a list except that it uses parentheses `()` instead of square brackets `[]`.

The following example defines a tuple called `rgb`:

```python
rgb = ('red', 'green', 'blue')
```
Once defining a tuple, you can access an individual element by its index. For example:
```python
rgb = ('red', 'green', 'blue')

print(rgb[0])
print(rgb[1])
print(rgb[2])
```
## Output:
red

green

blue

Since a **tuple is immutable**, you **cannot change its elements**. The following example attempts to change the first element of the rgb tuple to 'yellow':

```python
rgb = ('red', 'green', 'blue')
rgb[0] = 'yellow'
```
And it results in an error:

**TypeError:** 'tuple' object does not support item assignment

## Defining a Tuple that has One Element
To define a tuple with one element, you need to include a trailing comma after the first element. For example:

```python
numbers = (3,)
print(type(numbers))
```
**Output:**
`<class 'tuple'>`

If you **exclude the trailing comma, the type of the numbers will be int, which stands for integer. And its value is 3**. Python won’t create a tuple that includes the number 3:

```python
numbers = (3)
print(type(numbers))
```
## Output:
`<class 'int'>`

## Assigning a Tuple
Even though you can’t change a tuple, you can assign a new tuple to a variable that references a tuple. For example:

```python
colors = ('red', 'green', 'blue')
print(colors)

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)
```
## Summary
Tuples are immutable lists.

Use tuples when you want to define a list that cannot change.