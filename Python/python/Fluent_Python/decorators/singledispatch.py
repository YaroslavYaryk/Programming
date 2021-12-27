from functools import singledispatch

@singledispatch
def fun(arg):
    
    print("int called",arg)

@fun.register(str)
def _(arg):
    
    print("str called" ,arg)

@fun.register(list)
def _(arg):
    
    print("list called",arg)

@fun.register(int)
def _(arg):
    
    print("int called",arg)

fun(["3"])

