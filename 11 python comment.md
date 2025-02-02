# Python Comments

## Introduction to Python Comments
Sometimes, you want to document the code that you write. For example, you may want to note why a piece of code works. To do it, you use comments.

Typically, you use comments to explain formulas, algorithms, and complex business logic.

When executing a program, the Python interpreter ignores the comments and only interprets the code.

Python provides three kinds of comments:
- Block comments
- Inline comments
- Documentation strings (docstrings)

## Python Block Comments
A block comment explains the code that follows it. Typically, you indent a block comment at the same level as the code block.

To create a block comment, you start with a single hash sign (`#`) followed by a single space and a text string. For example:

```python
# increase price by 5%
price = price * 1.05
```

## Python Inline Comments
When you place a comment on the same line as a statement, you’ll have an inline comment.

Similar to a block comment, an inline comment begins with a single hash sign (`#`) and is followed by a space and a text string.

The following example illustrates an inline comment:

```python
salary = salary * 1.02   # increase salary by 2%
```

## Python Docstrings
A documentation string (docstring) is a string literal that you put as the first line(s) in a code block, for example, a function.

Unlike a regular comment, a documentation string can be accessed at run-time using `obj.__doc__`, where `obj` is the name of the function.

Typically, you use docstrings to automatically generate the code documentation.

### Types of Docstrings
Python provides two kinds of docstrings: one-line docstrings and multi-line docstrings.

#### 1) One-line Docstrings
As its name implies, a one-line docstring fits one line. A one-line docstring begins with triple quotes (`"""`) and ends with triple quotes (`"""`). There won’t be any blank line either before or after the one-line docstring.

The following example illustrates a one-line docstring in the `quicksort()` function:

```python
def quicksort():
    """ sort the list using quicksort algorithm """
    ...
```

#### 2) Multi-line Docstrings
Unlike a one-line docstring, a multi-line docstring can span multiple lines. A multi-line docstring also starts with triple quotes (`"""`) and ends with triple quotes (`"""`).

The following example shows how to use multi-line docstrings:

```python
def increase(salary, percentage, rating):
    """ 
    increase salary based on rating and percentage
    rating 1 - 2: no increase
    rating 3 - 4: increase 5%
    rating 4 - 6: increase 10%
    """
```

## Python Multiline Comments
Python doesn’t support multiline comments directly.

However, you can use multi-line docstrings as multiline comments. Guido van Rossum, the creator of Python, also recommended this approach.

It’s a good practice to keep your comments clear, concise, and explanatory. The ultimate goal is to save time and energy for you and other developers who will work on the code later.

## Summary
- Use comments to document your code when necessary.
- A block comment and inline comment start with a hash sign (`#`).
- Use docstrings for functions, modules, and classes.
