from string import ascii_letters
from numba import njit
import time

symbols = "1234567890!@#$%^&*()_+|\\}{[]';/?.,<>№"
ukr_lett = "абвгдежзиіїйклмнопрстуфхцчшщьюя"

ascii_letters += symbols + ukr_lett
@njit
def shifr(word):
    result = ""
    for i in ascii_letters:
        for j in ascii_letters:
            for k in ascii_letters:
                for l in ascii_letters:
                    if i + j + k + l == word:
                        result += i + j  + k + l
    return result                    


if __name__ == "__main__":
    word = input("enter a word: ")
    start = time.time()
    print(shifr(word))
    print(f"time is {time.time() - start} second")