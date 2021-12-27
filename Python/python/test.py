# from datetime import datetime


# class Time:
#     def __init__(self):
#         current_datetime = datetime.now()
#         self.__hours = current_datetime.hour
#         self.__minutes = current_datetime.minute
#         self.__seconds = current_datetime.second

#     def get_time1(self):
#         return f"\n{self.__hours} годин, {self.__minutes} хвилин, {self.__seconds} секунд"

#     def get_time2(self):
#         if self.__hours <= 12:
#             current_hours = self.__hours
#             str_hours = "a.m."
#         elif self.__hours >= 12:
#             current_hours = self.__hours - 12
#             str_hours = "p.m"
#         return f"\n{current_hours} {str_hours} {self.__minutes} хвилин, {self.seconds} секунд"

#     @property
#     def hours(self):
#         return self.__hours

#     @hours.setter
#     def hours(self, value):
#         if not isinstance(value, int) or not value:
#             raise TypeError("Hours must be integer!")
#         if not 0 <= value <= 23:
#             raise ValueError("Hours must be more than -1 and less than 24")
#         self.__hours = value

#     @property
#     def minutes(self):
#         return self.__minutes

#     @minutes.setter
#     def minutes(self, value):
#         if not isinstance(value, int) or not value:
#             raise TypeError("Minutes must be integer!")
#         if not 0 <= value <= 59:
#             raise ValueError("Minutes must be more than -1 and less than 24")
#         self.__minutes = value

#     @property
#     def seconds(self):
#         return self.__seconds

#     @seconds.setter
#     def seconds(self, value):
#         if not isinstance(value, int) or not value:
#             raise TypeError("Seconds must be integer!")
#         if not 0 <= value <= 59:
#             raise ValueError("Seconds must be more than -1 and less than 24")
#         self.__seconds = value


# time = Time()
# print(time.get_time1(), time.get_time2())


# import timeit
# import os.path
# import random

# file = open("text.txt", "w")
# while (os.path.getsize('text.txt')/(1024*1024)) < 50:
#     file.write(str(random.randint(0, 9)))

# text_readlines = """
# res = 0
# with open('text.txt') as file:
#     lines = file.readlines()
#     for i in lines:
#         if i.strip().isdigit():
#             res += int(i.strip())
# """
# print(timeit.timeit(stmt=text_readlines, number=50))

# text_for = """
# res = 0
# with open('text.txt') as file:
#     for line in file:
#         if line.strip().isdigit():
#             res += int(line.strip())
# """
# print(timeit.timeit(stmt=text_for, number=50))

# text = """
# with open('text.txt') as file:
#     res = sum((int(line.strip()) for line in file if line.strip().isdigit()))
# """
# print(timeit.timeit(stmt=text, number=50))


# def fact():
#     """here it is"""
#     storage = {}

#     def wrapper(n):
#         if not n:
#             return 1
#         if n not in storage:
#             storage[n] = wrapper(n - 1) * n
#         return storage[n]

#     return wrapper


# a = fact()
# print(a(5))
