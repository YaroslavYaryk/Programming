from random import randint

while True:
    try:
        num = int(input('size of matrix\n'))
        break
    except ValueError as error:
        print(error, "\ntry again")
first = []
while True:
    try:
        choose = int(input("by 1 - yourself  2 - random\n"))
        break
    except ValueError as error:
        print(error, "\n try again")

if choose == 1:

    def yourself(n):
        for i in range(n):
            c = []
            for j in range(n):
                c.append(int(input(f"a[{i + 1}][{j + 1}] ")))

            first.append(c)


    yourself(num)
elif choose == 2:

    def rand(n):
        for i in range(n):
            c = []
            for j in range(n):
                c.append(randint(0, 9))

            first.append(c)


    rand(num)


def number(n):
    k = 0
    for j in range(round((n + 1) / 2)):
        for i in range(j, n - j):
            if first[i][j] == 0:
                k += 1
        return k


number(num)
print(f"number of NULL is {number(num)}")


def beautiful_print(num):
    for i in range(num):
        for j in range(num):
            if i + j <= num - 1 and i - j >= 0:
                print(f"*{first[i][j]}*", end='')
            else:
                print(f" {first[i][j]} ", end='')
        print("")


beautiful_print(num)


def s5d(n):
    numb = 0
    for i in range(n - 1):
        for j in range(n - i - 1):
            first[i][j] = 0
            numb += 1

    return numb


s5d(num)
print(f"number of 5 sector is {s5d(num)}")


def show(n):
    for i in range(n):
        for j in range(n):
            print(first[i][j], end='  ')
        print()


show(num)
