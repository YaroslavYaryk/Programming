class NonNegative(object):
    def __set_name__(self,owner,name):
        self.name = name
    def __get__(self,instance,owner):    
        return instance.__dict__[self.name]

    def __set__(self,instance,value):
        if value < 0:
            raise ValueError("can't be negative")
        else:
            instance.__dict__[self.name] = value

class Check_int_float(object):

    @staticmethod
    def checker(value):
        return isinstance(value, (int, float))

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if Check_int_float.checker(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("must be int or float")


class Check_string(object):

    @staticmethod
    def __check(value):
        return isinstance(value, str)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if Check_string.__check(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("must be string ")