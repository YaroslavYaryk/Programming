import operator

def input_operation():
    operation = input("enter +, -, *, /, ^, 'exit' to quit ")

    if operation == "+":
        return operator.add
    elif operation == "-":
        return operator.sub
    elif operation == "/":
        return operator.truediv
    elif operation == "*":
        return operator.mul
    elif operation == "^":
        return operator.pow
    elif operation == "exit":
        exit()
    else:
        raise NotImplementedError


def mult():
    operation = input_operation()


    first = int(input("first one: "))
    second = int(input("second one"))
    result = operation(first,second)
    print(result)


mult()    