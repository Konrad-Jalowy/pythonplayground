class Greeting:
    name = "stranger"
    def __init__(self, greeting):
        self.greeting = greeting

    def __repr__(self):
        return self.greeting

    def __format__(self, format_spec):
        if format_spec == "again":
            return f"{self.greeting} again!"
        elif format_spec == "angry":
            return f"{self.greeting} asshole..."
        elif format_spec == "name":
            return f"{self.greeting} {Greeting.name}"
        elif format_spec == "ask":
            name = input("Hi, whats your name?\n")
            Greeting.name = name
            return "Ill remember that. Nice to meet you"
    @classmethod
    def setName(cls, name):
        cls.name = name


hi = Greeting("Hi")
print(hi)
print(f"{hi:again}")
print(f"{hi:angry}")
print(f"{hi:name}")
print(f"{hi:ask}")
print(f"{hi:name}")