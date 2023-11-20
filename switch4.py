import random


class SwitchPython:

    def __init__(self):
        self.cases = dict()
        self.default = None

    def add_case(self, case, func):
        self.cases[case] = func
        return self

    def add_default(self, func):
        self.default = func
        return self

    def get_case(self, val):
        func = self.cases.get(val, self.default)
        return func()

    def add_cases(self, new_cases):
        self.cases.update(new_cases)
        return self


my_switch = SwitchPython()
my_switch.add_case(1, lambda: "case 1").add_case(2, lambda: "case 2").add_case(3, lambda: "case 3")
my_switch.add_case(4, lambda: "case 4").add_cases({
    5: lambda : "case 5",
    6: lambda : "case 6"
}).add_default(lambda: "default")
number = random.randint(1,6)
res = my_switch.get_case(7)
print(res)