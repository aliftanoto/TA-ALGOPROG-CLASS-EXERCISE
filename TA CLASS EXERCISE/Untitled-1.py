# Encapsulation: Using classes to encapsulate data and methods

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


# Inheritance: Creating a new class by inheriting from a base class

class Dog(Animal):
    def make_sound(self):
        return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Polymorphism (Overriding): Objects of different classes responding to the same method

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())


# Abstraction: Hiding complex implementation details

class Shape:
    def calculate_area(self):
        raise NotImplementedError("Subclasses must implement calculate_area method.")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# Example usage:

# Encapsulation
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.make_sound())
print(cat.make_sound())

# Polymorphism (Overriding)
animals = [dog, cat]
animal_sounds(animals)

