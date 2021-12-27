import string
from tqdm import tqdm
from time import sleep


def funk():
    print("tarnsporting...")
    for i in tqdm(list(range(0,101))):
        sleep(0.1)


def main():
    alphabet = str(string.ascii_lowercase) * 2

    def codding():
        a = input('shifr or deshifr:\n')
        if a == 'shifr':
            print('cesar or wilinger or perestanovka? ')
            method = input('enter the method :\n')

            def shifd(method):
                if method == 'wilinger':
                    n = input('enter what you wanna shifr\n')
                    k = input('enter the word:\n')

                    def wilinger(n, k):
                        d = ' ' + k * 10
                        shifr = ''
                        for letter in n:
                            position = alphabet.find(letter)
                            n = 1
                            position2 = alphabet.find(d[n])
                            new_position = position + position2
                            if letter in alphabet:
                                shifr += alphabet[new_position]
                            else:
                                shifr += letter
                            n += 1
                        return shifr
                    funk()
                    print(wilinger(n, k))

                elif method == 'cesar':
                    word = input('what do you wanna shifr:\n')
                    while True:
                        try:
                            key = int(input('key= '))
                            break
                        except ValueError as error:
                            print(error)

                    def cesar(word, key):

                        sss = ''
                        a = string.ascii_lowercase
                        alphabet = a * 2
                        for i in word:
                            position = a.find(i)
                            new_position = position + key
                            if i in alphabet:
                                sss += alphabet[new_position]
                            else:
                                sss += i
                        return sss
                    
                    funk()
                    print(cesar(word, key))

                if method == 'perestanovka':
                    word = input('enter the word what you wanna shifr:\n')

                    def perestanovka(word):
                        shifr = ''

                        k = (len(word) // 2)

                        a = 0
                        # b = 2
                        n = 0
                        for j in range(k):
                            shifr += word[a]
                            shifr += word[k + n]
                            a += 1
                            # b += 1
                            n += 1

                        return shifr

                    funk()
                    print(perestanovka(word))

            shifd(method)

        elif a == 'deshifr':
            print('cesar or wilinger?')
            method = input('enter the method:\n')

            def deshifr(method):
                if method == 'wilinger':
                    n = input('enter what you wanna deshifr\n')
                    k = input('enter the word\n')

                    def wilinger(n, k):
                        d = ' ' + k * 10
                        method = input()
                        shifr = ''
                        for letter in n:
                            position = alphabet.find(letter)
                            n = 1
                            position2 = alphabet.find(d[n])
                            new_position = position - position2
                            if letter in alphabet:
                                shifr += alphabet[new_position]
                            else:
                                shifr += letter
                            n += 1
                        return shifr
                    
                    funk()
                    print(wilinger(n, k))

                elif method == 'cesar':
                    word = input('what do you wanna deshifr:\n')
                    while True:
                        try:
                            key = int(input('key=\n'))
                            break
                        except ValueError as error:
                            print(error)

                    def cesar(word, key):

                        sss = ''
                        a = string.ascii_lowercase
                        alphabet = a * 2
                        for i in word:
                            position = a.find(i)
                            new_position = position - key
                            if i in alphabet:
                                sss += alphabet[new_position]
                            else:
                                sss += i
                        return sss

                    funk()
                    print(cesar(word, key))
                else:
                    print('there is no such function')

            deshifr(method)

        else:
            print('there are no such methods')

    codding()


main()
