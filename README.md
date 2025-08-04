# OOP

# Object-Oriented Programming (OOP) Assignments 🏗️

A comprehensive Python project demonstrating the four core principles of Object-Oriented Programming through interactive superhero and vehicle classes.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Class Structure](#class-structure)
- [OOP Concepts Demonstrated](#oop-concepts-demonstrated)
- [Code Examples](#code-examples)
- [Contributing](#contributing)

## 🎯 Overview

This project contains two main assignments that showcase fundamental OOP concepts:

1. **Assignment 1**: A superhero class system with inheritance and encapsulation
2. **Assignment 2**: A vehicle polymorphism challenge demonstrating method overriding


## ✨ Features

- **Complete Class Hierarchy**: Base classes with multiple inheritance levels
- **Encapsulation**: Private and protected attributes with controlled access
- **Polymorphism**: Same method names with different implementations
- **Constructor Patterns**: Flexible object initialization
- **Method Overriding**: Specialized behavior in child classes
- **Interactive Demonstrations**: Built-in examples showing all concepts


```bash
# Run the program
python oop.py
```

## 🎮 Usage

### Basic Usage

```python
# Import the classes
from oop_assignments import Superhero, FlyingHero, Car, Plane

# Create superhero instances
superman = FlyingHero("Superman", "Clark Kent", 95, 1000)
iron_man = TechHero("Iron Man", "Tony Stark", 80, 10)

# Use their powers (polymorphism in action)
superman.use_power()  # Output: "Superman soars through the sky at 1000 mph! 🦅"
iron_man.use_power()  # Output: "Iron Man deploys advanced technology and gadgets! 🔧"

# Create vehicle instances
car = Car("Tesla", 155, "electric")
plane = Plane("Boeing 747", 570, 35000)

# Make them move (polymorphism)
car.move()    # Output: "Tesla is driving on the road at 155 mph! 🚗"
plane.move()  # Output: "Boeing 747 is flying through the sky at 570 mph at 35000 feet! ✈️"
```

### Running the Full Demo

```python
# Run the complete demonstration
python oop_assignments.py
```

This will execute both assignments and show all OOP concepts in action.

## 🏗️ Class Structure

### Assignment 1: Superhero System

```
Superhero (Base Class)
├── FlyingHero
├── StrengthHero
└── TechHero
```

**Base Class - Superhero:**
- Attributes: `name`, `real_name`, `_power_level`, `__secret_weakness`
- Methods: `get_power_level()`, `train()`, `use_power()`, `introduce()`

**Child Classes:**
- **FlyingHero**: Adds flight capabilities and rescue methods
- **StrengthHero**: Adds super strength and barrier-breaking abilities
- **TechHero**: Adds technology features and gadget management

### Assignment 2: Vehicle System

```
Vehicle (Base Class)
├── Car
├── Plane
├── Boat
└── Bicycle
```

**All vehicles inherit from Vehicle and override the `move()` method.**

## 🎓 OOP Concepts Demonstrated

### 1. **Encapsulation** 🔒
```python
class Superhero:
    def __init__(self, name, real_name, power_level=50):
        self.name = name                    # Public
        self._power_level = power_level     # Protected
        self.__secret_weakness = "Unknown"  # Private
    
    def get_power_level(self):  # Controlled access
        return self._power_level
```

### 2. **Inheritance** 👑
```python
class FlyingHero(Superhero):  # Inherits from Superhero
    def __init__(self, name, real_name, power_level=50, flight_speed=100):
        super().__init__(name, real_name, power_level)  # Call parent constructor
        self.flight_speed = flight_speed  # Add new attribute
```

### 3. **Polymorphism** 🎭
```python
# Same method name, different implementations
def use_power(self):
    # In FlyingHero:
    print(f"{self.name} soars through the sky! 🦅")
    
    # In StrengthHero:
    print(f"{self.name} lifts enormous objects! 💪")
    
    # In TechHero:
    print(f"{self.name} deploys advanced technology! 🔧")
```

### 4. **Constructor Patterns** 🛠️
```python
def __init__(self, name, real_name, power_level=50):
    # Initialize with default values
    # Accept parameters for customization
    # Set up initial state
```

## 💡 Code Examples

### Creating and Using Superheroes

```python
# Create different types of heroes
superman = FlyingHero("Superman", "Clark Kent", 95, 1000)
hulk = StrengthHero("The Hulk", "Bruce Banner", 90, 50)

# Train your hero (encapsulation in action)
superman.train(5)  # Increases power level safely

# Polymorphism - same call, different behavior
heroes = [superman, hulk]
for hero in heroes:
    hero.use_power()  # Each hero acts differently!
```

### Vehicle Polymorphism Challenge

```python
# Create different vehicles
vehicles = [
    Car("Tesla", 155),
    Plane("Boeing 747", 570),
    Boat("Yacht", 45),
    Bicycle("Mountain Bike", 25)
]

# Polymorphism in action
for vehicle in vehicles:
    vehicle.move()  # Each vehicle moves differently!
```

## 🎯 Learning Objectives

After studying this code, you should understand:

- ✅ How to create classes with constructors
- ✅ How to implement encapsulation with private/protected attributes
- ✅ How inheritance creates "is-a" relationships
- ✅ How polymorphism allows different objects to respond to the same method call
- ✅ How to design class hierarchies
- ✅ How to override methods in child classes
- ✅ How to use `super()` to call parent class methods

## 🔧 Extending the Code

### Add New Superhero Types
```python
class MagicHero(Superhero):
    def use_power(self):
        print(f"{self.name} casts magical spells! ✨")
```

### Add New Vehicle Types
```python
class Motorcycle(Vehicle):
    def move(self):
        print(f"{self.name} is cruising on two wheels! 🏍️")
```

## 📚 Educational Notes

- **Encapsulation**: Notice how `_power_level` is protected and accessed through methods
- **Inheritance**: Child classes extend parent functionality without duplicating code
- **Polymorphism**: The beauty of calling the same method on different objects
- **Code Reuse**: Parent class methods are inherited and can be extended or overridden


---

**Happy Coding!** 🚀 Remember: Good OOP design makes code more maintainable, reusable, and easier to understand!
