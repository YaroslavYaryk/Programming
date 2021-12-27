class Person(object):

    def __init__(self):

        self._first_name = "Yaroslav"
        self._last_name = "Dyhanov"


def upper_case_name(obj):

    return (f"{obj._first_name} {obj._last_name}").upper() 

upper_case_name.short_description = "Customer name"

obj = Person()
print(upper_case_name(obj))
print(upper_case_name)