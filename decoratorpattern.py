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

# Usage
coffee = SimpleCoffee()
print(f"Cost of simple coffee: ${coffee.cost()}")

milk_coffee = MilkDecorator(coffee)
print(f"Cost of milk coffee: ${milk_coffee.cost()}")

sugar_milk_coffee = SugarDecorator(milk_coffee)
print(f"Cost of sugar milk coffee: ${sugar_milk_coffee.cost()}")