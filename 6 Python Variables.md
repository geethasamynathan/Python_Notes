# Python Variables
## What is a variable in Python
When you develop a program, you need to manage values, a lot of them. To store values, you use variables.

In Python, a variable is a label that you can assign a value to it. And a variable is always associated with a value. For example:
```python
message = 'Hello, World!'
print(message)

message = 'Good Bye!'
print(message)
```


### Output:

`Hello, World!`
`Good Bye!`

In this example, message is a variable. It holds the string 'Hello, World!'. The print() function shows the message Hello, World! to the screen.

The next line assigns the string 'Good Bye!' to the message variable and print its value to the screen.

The variable message can hold various values at different times. And its value can change throughout the program.

### Creating variables
To define a variable, you use the following syntax:

`variable_name = value`

The = is the assignment operator. In this syntax, you assign a value to the variable_name.

The value can be anything like a number, a string, etc., that you assign to the variable.

The following defines a variable named counter and assigns the number 1 to it:
```python
counter = 1
```
### Naming variables
When you name a variable, you need to adhere to some rules. If you don’t, you’ll get an error.

The following are the variable rules that you should keep in mind:

Variable names can contain only letters, numbers, and underscores (_). They can start with a letter or an underscore (_), not with a number.

Variable names cannot contain spaces. To separate words in variables, you use underscores for example sorted_list.

Variable names cannot be the same as keywords, reserved words, and built-in functions in Python.

The following guidelines help you define good variable names:

Variable names should be concise and descriptive. For example, the active_user variable is more descriptive than the au.

Use underscores (_) to separate multiple words in the variable names.

Avoid using the letter l and the uppercase letter O because they look like the number 1 and 0.