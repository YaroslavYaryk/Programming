# """this library helps you find a weak poin of your code
# by testing it"""
import cProfile
# from time import sleep

# def rec_factorial(x):
#     if x == 0:
#         return 1

#     else:
#         return rec_factorial(x-1) * x


# def factorial_iter(x):
#     storage = 1
#     for i in range(2,x+1):
#         storage *=i
#     return storage    

# def main():

#     rec_factorial(100)
#     factorial_iter(100)



# cProfile.run("main()")    


import random
def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()

def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()


def main():
    sort_expensive()
    for i in range(1000):
        sort_cheap()

cProfile.run("main()")    
