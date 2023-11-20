def miniswitch(val):
    return {
        'a' : 1,
        'b' : 2
    }.get(val, 0)

print(miniswitch('a'))
print(miniswitch('b'))
print(miniswitch('c'))
val2 = 'b'
print({'a': 1,
       "b": 2}.get(val2, 0))