class StringFunctor:
    def __init__(self, value):
        self.value = value
        self.allowed = ['upper', 'lower', 'capitalize']

    def __call__(self, f):
        return f(self.value) if f.__name__ in self.allowed else self.value


def uppercase(s):
    return s.upper()


functor = StringFunctor("hello")
print(functor(str.upper))
print(functor(str.lower))
print(functor(str.capitalize))
print(functor(str.swapcase))
print(functor(uppercase))