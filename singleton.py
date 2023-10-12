class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
        return cls._instance

# Usage
singleton1 = Singleton()
singleton1.value = "First Instance"

singleton2 = Singleton()
singleton2.value = "Second Instance"

print(singleton1.value)  # Output: "Second Instance"
print(singleton2.value)  # Output: "Second Instance"

# Both singleton1 and singleton2 are the same instance
print(singleton1 is singleton2)  # Output: True