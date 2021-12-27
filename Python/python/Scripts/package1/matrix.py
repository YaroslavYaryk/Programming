import random
word = input('suma or transpose\nwhat do you wanna do?:\n')
while True:
    try:
        size = int(input('size: '))
        break

    except ValueError:
        print("The wrong type of files")



first_matrix = []
second_matrix = []
result = []


def printa(size, matr):
    for i in range(size):
        for j in range(size):
            print(matr[i][j], end='\t\t')
        print('\n')


def yourself(size, matr):
    print('enter the elements of second matrix')
    for i in range(size):
        c = []
        for j in range(size):
            c.append(int(input(f'a[{i + 1}][{j + 1}]')))
        matr.append(c)


def rand(n, matr):
    for i in range(n):
        c = []
        for j in range(n):
            c.append(random.randint(0, 9))

        matr.append(c)


if word == "suma":
    choise = input("random or by yourself?")
    if choise == "yourself":

        yourself(size, first_matrix)
        print("the first one is:")

        printa(size, first_matrix)

        yourself(size, second_matrix)
        print("the second one is:")

        printa(size, second_matrix)
    elif choise == "random" or 1:

        rand(size, first_matrix)
        print("the first one is:")
        printa(size, first_matrix)

        rand(size, second_matrix)
        print("the the second  one is:")

        printa(size, second_matrix)


    def sum(s):
        for i in range(s):
            c = []
            for j in range(s):
                c.append('0')
            result.append(c)

        for i in range(s):
            for j in range(s):
                result[i][j] = first_matrix[i][j] + second_matrix[i][j]


    sum(size)
    print('the sum is:')
    printa(size, result)

elif word == 'transpose':

    def trans(size):
        a = input("b - by yourself or r - random:\n")
        if a == "b":
            yourself(size, first_matrix)
        elif a == "r":
            rand(size, first_matrix)
        print('the matrix  is:')
        printa(size, first_matrix)
        for i in range(size):
            c = []
            for j in range(size):
                c.append('0')
            result.append(c)

        for i in range(size):
            for j in range(size):
                result[j][i] = first_matrix[i][j]


    trans(size)
    print('the transpose is:')
    printa(size, result)
else:
    print('there is no such operation')
