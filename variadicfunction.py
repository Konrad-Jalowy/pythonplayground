def sum(*args):
    sum = 0
    for n in args:
        sum+= n
    return sum

print(sum(1,4,1,11))