import random


class SwitchPython:

    def __init__(self):
        self.cases = dict()
        self.default = None

    def __call__(self, val):
        func = self.cases.get(val, self.default)
        return func()

    def add_case(self, case, func):
        self.cases[case] = func
        return self

    def add_default(self, func):
        self.default = func
        return self

    def add_cases(self, new_cases):
        self.cases.update(new_cases)
        return self


number = random.randint(1, 7)
res = SwitchPython()\
    .add_case(1, lambda: "case 1")\
    .add_case(2, lambda: "case 2")\
    .add_case(3, lambda: "case 3")\
    .add_case(4, lambda: "case 4")\
    .add_cases({
    5: lambda : "case 5",
    6: lambda : "case 6"
}).add_default(lambda: "default")(number)
print(res)