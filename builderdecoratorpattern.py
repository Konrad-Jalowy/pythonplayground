# Component interface
class Coffee:
    def cost(self):
        pass

# Concrete Component
class SimpleCoffee(Coffee):
    def cost(self):
        return 5  # Base cost of a simple coffee

# Decorator
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Concrete Decorators
class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 2  # Add cost of milk

class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return super().cost() + 1  # Add cost of sugar

# Builder for creating decorated coffee
class CoffeeBuilder:
    def __init__(self):
        self._coffee = SimpleCoffee()

    def add_coffee(self):
        return self

    def add_milk(self):
        self._coffee = MilkDecorator(self._coffee)
        return self

    def add_sugar(self):
        self._coffee = SugarDecorator(self._coffee)
        return self

    def build(self):
        return self._coffee

# Usage with the builder
coffee = CoffeeBuilder().add_coffee().add_milk().add_sugar().build()
print(f"Cost of custom coffee: ${coffee.cost()}")