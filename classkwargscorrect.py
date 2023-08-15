class Person:
    def __init__(self, **kwargs):
        self.first_name = kwargs.get("first_name", "Unknown")
        self.last_name = kwargs.get("last_name", "Unknown")