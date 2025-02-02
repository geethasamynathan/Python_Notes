# Python Syntax
## Whitespace and indentation
If you’ve been working in other programming languages such as Java, C#, or C/C++, you know that these languages use semicolons (;) to separate the statements.

However, Python uses **whitespace and indentation** to construct the code structure.

The following shows a snippet of Python code:
```python
# define main function to print out something
def main():
    i = 1
    max = 10
    while (i < max):
        print(i)
        i = i + 1

# call function main 
main()
```
The meaning of the code isn’t important to you now. Please pay attention to the code structure instead.

At the end of each line, yo**u don’t see any semicolon** to terminate the statement. And the code uses indentation to format the code.

By using indentation and whitespace to organize the code, Python code gains the following advantages:

First, you’ll never miss the beginning or ending code of a block like in other programming languages such as Java or C#.

Second, the **coding style is essentially uniform**. If you have to maintain another developer’s code, that code looks the same as yours.

Third, the code is more readable and clear in comparison with other programming languages.

# Comments
The comments are as important as the code because they describe why a piece of code was written.

When the Python interpreter executes the code, it ignores the comments.

In Python, a single-line comment begins with a hash (#) symbol followed by the comment. For example:
```python
# This is a single line comment in Python
```
And Python also supports other kinds of comments.

Continuation of statements
Python uses a newline character to separate statements. It places each statement on one line.

However, a long statement can span multiple lines by using the backslash (\) character.

The following example illustrates how to use the backslash (\) character to continue a statement in the second line:
```python
if (a == True) and (b == False) and \
   (c == True):
    print("Continuation of statements")
```
# Identifiers
Identifiers are names that **identify variables, functions, modules, classes, and other objects** in Python.

The name of an identifier needs to **begin with a letter or underscore (_)**. The following characters can be alphanumeric or underscore.

**Python identifiers are case-sensitive**. For example, the counter and Counter are different identifiers.

In addition, you cannot use Python keywords for naming identifiers.

Keywords
Some words have special meanings in Python. They are called keywords.

The following shows the list of keywords in Python:
```python
False      class      finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise
```
Python is a growing and evolving language. So its keywords will keep increasing and changing.

Python provides a special module for listing its keywords called keyword. 

To find the current keyword list, you use the following code:
```python
import keyword
print(keyword.kwlist) 
print(len(keyword.kwlist))
```
# String literals
Python uses single quotes ('), double quotes ("), triple single quotes (''') and triple-double quotes (""") to denote a string literal.

The string literal need to be surrounded with the same type of quotes. For example, if you use a single quote to start a string literal, you need to use the same single quote to end it.

The following shows some examples of string literals:
```python
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)
```
# Summary
A Python statement ends with a newline character.

Python uses spaces and indentation to organize its code structure.

Identifiers are names that identify variables, functions, modules, classes, etc. in Python.

Comments describe why the code works. They are ignored by the Python interpreter.

Use the single quote, double-quotes, triple-quotes, or triple double-quotes to denote