import string

alfa = string.ascii_letters


word = input('what do you wanna do:\nalphabet or mine2 or bulb_sort\n')
def main():
    if word == "alphabet" :
        arr1 = list(input('what do you wanna get rid of'))
        arr2 = []

        def alphabet(arr1, arr2):
            for i in arr1:
                if i in alfa:
                    arr2.append(i)
                else:
                    continue
            for i in arr2:
                print(i, end='')

        alphabet(arr1, arr2)
    elif word == "mine2":
        storage = []

        def mine2():
            print("enter 10 words which you wanna turn into alphabet order:")
            for i in range(1, 11):
                w = input(f"word {i}:")
                storage.append(w)
            print('the precious one:\n')
            for j in storage:
                print(j, end=' ')

            print("\nthe new one is:")
            for p in sorted(storage):
                print(p, end=' ')

        (mine2())

    elif word == "bulb_sort":

        storage = []

        def bulb():
            for i in range(1, 10):
                w = int(input(f"figure {i}:"))
                storage.append(w)
            for j in range(len(storage) - 1):
                for k in range(len(storage) - 1 - j):
                    if storage[k] > storage[k + 1]:
                        storage[k], storage[k + 1] = storage[k + 1], storage[k]
            for ll in storage:
                print(ll, end=' ')

        bulb()
    else:
        print('no way , man')


main()
