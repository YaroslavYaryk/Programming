import prettytable
from math import sin,cos
# a, b, c  = input("someth: ").split()
# def table(*args):

#     pretty = prettytable.PrettyTable()
#     pretty.field_names = [args[0],args[1], args[2]]
#     a, b,c  = input("enter: ").split()
#     pretty.add_row([a, b,c])
#     return pretty
# print(table(a,b,c))


pretty_one = prettytable.PrettyTable()
pretty_one.field_names = ["x", "sin(x)", "cos(x)"]
i = 0
# pretty_one.align = "l"
while i <= 1:
    i = round(i, 2)
    pretty_one.add_row([i, round(sin(i),3), round(cos(i),3)])
    i+=0.1

print(pretty_one.get_string())