a = [i ** 2 for i in range(10)]
print(a)


q = (
    lambda l: q([x for x in l[1:] if x <= l[0]])
    + [l[0]]
    + q([x for x in l if x > l[0]])
    if l
    else []
)


print(q([1, 4, 77, 8, 6, 5, 4, 3, 7, 8]))

print((lambda x: x + 3)(19))
