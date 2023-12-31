class NumberFunctor:
   def __init__(self, value):
      self.value = value
        
   def __call__(self, f):
      return f(self.value)
    
def square(x):
   return x * x

functor = NumberFunctor(5)
result = functor(square)
print(result)

class StringFunctor:
   def __init__(self, value):
      self.value = value
        
   def __call__(self, f):
      return f(self.value)
    
def uppercase(s):
   return s.upper()

functor = StringFunctor("hello")
result = functor(uppercase)
print(result)

