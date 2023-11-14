class Greeting:

    def __init__(self, greeting):
        self.greeting = greeting
        self.personalInfo = PersonalInfo()

    def __repr__(self):
        return self.greeting

    def __format__(self, format_spec):
        if format_spec == "again":
            return f"{self.greeting} again!"
        elif format_spec == "angry":
            return f"{self.greeting} asshole..."
        elif format_spec == "name":
            return f"{self.greeting} {self.personalInfo.name}"
        elif format_spec == "ask":
            return self.personalInfo.ask_name()
        elif format_spec == "sex" and self.personalInfo.gender:
            return f"{self.greeting} {'bro!' if self.personalInfo.gender == 'M' else 'sis!'}"


class PersonalInfo:
    def __init__(self):
        self.name = "stranger"
        self.gender = None

    def ask_name(self):
        name = input("Whats your name?\n")
        self.name = name
        return "Ill remember that. Nice to meet you"

    def set_gender(self, val):
        self.gender = val


hi = Greeting("Hi")
print(hi)
print(f"{hi:again}")
print(f"{hi:angry}")
print(f"{hi:name}")
print(f"{hi:ask}")
print(f"{hi:name}")
hi.personalInfo.gender = 'M'
print(f"{hi:sex}")