n = int(input("n: "))
def eratosfen(n):
    A = list(range(n))
    A[0] = A[1] = 0
    for i in range(2,n):
        if A[i]:
            for j in range(i + i, n, i ):
                A[j] = 0

    return A

print(eratosfen(n))

