2. Polymorphism (Poly)

# Introduction
Polymorphism allows objects of different classes to be treated as objects of a common superclass. It enables methods to behave differently based on the object that calls them.

# Purpose
- Flexibility: Write code that can work with objects of multiple types.
- Simplicity: Use a single interface to represent different types of objects.

# Different Options with Examples

 1. Method Overriding
A child class provides a specific implementation of a method already defined in the parent class.

```python
# Parent Class
class Animal:
    def speak(self):
        return "Animal sound"

# Child Class
class Cat(Animal):
    def speak(self):
        return "Meow"

# Example
animal = Animal()
cat = Cat()
print(animal.speak())  # Output: Animal sound
print(cat.speak())     # Output: Meow
```

 2. Method Overloading
Python does not support method overloading directly, but it can be achieved using default arguments or variable-length arguments.

```python
class MathOperations:
    def add(self, a, b, c=0):
        return a + b + c

# Example
math = MathOperations()
print(math.add(2, 3))       # Output: 5
print(math.add(2, 3, 4))    # Output: 9
```

 3. Duck Typing
Python uses duck typing, where the type or class of an object is determined by its behavior (methods and properties) rather than its inheritance.

```python
class Duck:
    def quack(self):
        return "Quack!"

class Person:
    def quack(self):
        return "I can quack like a duck!"

def make_it_quack(obj):
    print(obj.quack())

# Example
duck = Duck()
person = Person()
make_it_quack(duck)    # Output: Quack!
make_it_quack(person)  # Output: I can quack like a duck!
```

