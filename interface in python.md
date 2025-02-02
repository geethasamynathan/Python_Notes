# Python Interface - Complete Explanation with Examples
Unlike some other languages like Java and C#, Python does not have a built-in keyword for interfaces. However, we can achieve interface-like behavior using Abstract Base Classes (ABCs) from the `abc` module.
## 1. What is an Interface in Python?
- An **interface** defines a set of methods that a class **must implement**, but it does not provide any implementation itself.
- Interfaces help in **enforcing a contract** for classes that inherit from them.
- In Python, **Abstract Base Classes (ABCs)** serve as interfaces.
## 2. Creating an Interface in Python
We use `ABC` (Abstract Base Class) and `@abstractmethod` to define an interface.
## Example 1: Basic Interface
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Bark!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark!
print(cat.make_sound())  # Output: Meow!
```
## 3. Enforcing Multiple Interfaces
### Example 2: Multiple Interfaces
```python
from abc import ABC, abstractmethod

class Flyer(ABC):
    @abstractmethod
    def fly(self):
        pass

class Swimmer(ABC):
    @abstractmethod
    def swim(self):
        pass

class Duck(Flyer, Swimmer):
    def fly(self):
        return "Duck is flying."

    def swim(self):
        return "Duck is swimming."

duck = Duck()
print(duck.fly())   # Output: Duck is flying.
print(duck.swim())  # Output: Duck is swimming.
```

##  4. Using Default Implementations in Interfaces
## Example 3: Default Implementation
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def max_speed(self):
        pass

    def start_engine(self):
        return "Engine started."

class Car(Vehicle):
    def max_speed(self):
        return 200

car = Car()
print(car.start_engine())  # Output: Engine started.
print(car.max_speed())     # Output: 200
```
 5. Preventing Object Creation with Interfaces
An interface **cannot be instantiated** directly.
### Example:
v = Vehicle()  # TypeError: Can't instantiate abstract class Vehicle

## 6. Interface with Class Variables
### Example 4: Constants in Interfaces
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    PI = 3.14159  # Constant

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Shape.PI * self.radius ** 2

c = Circle(5)
print(f"Area of Circle: {c.area()}")  # Output: 78.53975
```
## 7. Using Python’s `Protocol` for Interfaces
Starting from **Python 3.8**, we can use the `typing.Protocol` module to create interfaces.
###  Example 5: Using `Protocol` as an Interface
```python 
from typing import Protocol

class Walkable(Protocol):
    def walk(self) -> str:
        ...

class Person:
    def walk(self) -> str:
        return "Person is walking."

class Robot:
    def walk(self) -> str:
        return "Robot is walking."

p = Person()
r = Robot()

print(p.walk())  # Output: Person is walking.
print(r.walk())  # Output: Robot is walking.
```
Summary Table of Interface Methods in Python
| **Feature**                         | **`ABC` (Abstract Base Class)** | **`Protocol`**          |
|-------------------------------------|---------------------------------|-------------------------|
| **Forces method implementation**    | ✅ Yes                          | ✅ Yes                  |
| **Allows multiple inheritance**     | ✅ Yes                          | ✅ Yes                  |
| **Supports concrete methods**       | ✅ Yes                          | ❌ No                   |
| **Available from Python**           | ✅ Any version                  | ✅ Python 3.8+           |
| **Supports static typing**          | ❌ No                           | ✅ Yes                  |

Conclusion
- **Abstract Base Classes (`ABC`)** allow us to define interfaces in Python.
- **Multiple interfaces** can be implemented using multiple inheritance.
- **Default implementations** can be provided inside abstract classes.
- **`Protocol` (from `typing` module)** is an alternative for defining interfaces with static type checking.
