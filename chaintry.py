from itertools import chain
x = [1, 2]
y = [3, 4]
z = range(5,11)

for i in chain(x, y, z, (num for num in range(11,21))):
    print(i)