from abc import ABC, abstractmethod

# Abstract Product
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

# Concrete Products
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Abstract Factory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

# Concrete Factories
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Client
def animal_sound(factory):
    animal = factory.create_animal()
    return animal.speak()

# Usage
dog_factory = DogFactory()
cat_factory = CatFactory()

print(animal_sound(dog_factory))  # Output: "Woof!"
print(animal_sound(cat_factory))  # Output: "Meow!"