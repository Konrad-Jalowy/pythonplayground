import random


class SwitchPython:

    def __init__(self):
        self.cases = dict()

    def add_case(self, case, func):
        self.cases[case] = func
        return self

    def get_case(self, val):
        func = self.cases.get(val, None)
        return func()

    def add_cases(self, new_cases):
        self.cases.update(new_cases)


my_switch = SwitchPython()
my_switch.add_case(1, lambda: "case 1")
my_switch.add_case(2, lambda: "case 2")
my_switch.add_case(3, lambda: "case 3")
my_switch.add_case(4, lambda: "case 4")
my_switch.add_cases({
    5: lambda : "case 5",
    6: lambda : "case 6"
})
# number = random.randint(1,4)
number = 6
res = my_switch.get_case(number)
print(res)
