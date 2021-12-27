import time

# def add_file(funk):

#     def Wrapper(*args, **kwargs):
#         print("start downloading")
#         for i in range(5):
#             print("downloading...")
#             time.sleep(1)
#         with open("log.txt", "w") as f:
#             f.write(funk(*args, **kwargs))
#         time.sleep(3)
#         print("finish downloading") 
#     return Wrapper

# @add_file
# def Someth_writer(text):
#     if isinstance(text, str):

#         if len(text) <= 100:
#             return text
#         else:
#             raise OutOfMemoryError    
#     else:
#         raise ValueError("must be string")

# (Someth_writer("hello world"))
# with open("log.txt", "r") as f:
#     print(f.read())
