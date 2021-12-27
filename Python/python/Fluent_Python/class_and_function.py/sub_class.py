import weakref

class My_list(list):
    pass

a = My_list(range(10))

ref_to_a = weakref.ref(a)
print(ref_to_a)
del a
print(ref_to_a)

print(list("hello"))