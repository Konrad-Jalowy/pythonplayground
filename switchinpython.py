import random


class SwitchPython:
    
    def __init__(self):
        self.cases = {}

    def add_case(self, case, func):
        self.cases[case] = func
        return self
    
    def get_case(self, val):
        func = self.cases.get(val, None)
        return func()


my_switch = SwitchPython()
my_switch.add_case(1, lambda: "case 1")
my_switch.add_case(2, lambda: "case 2")
my_switch.add_case(3, lambda: "case 3")
my_switch.add_case(4, lambda: "case 4")
number = random.randint(1,4)
res = my_switch.get_case(number)
print(res)
