import random
import time


alphabet = "abcdefghijklmnopqrstuvwxyz "
first = ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
second = ["", "", "", "", "", "", "", "", "", "", ""]
a = 0
while a<len(second):
    if second[a] != first[a]:
        second[a] = random.choice(alphabet)

    if second[a] == first[a]:
        a += 1
    print(second[a], end= "")

    time.sleep(.2)

