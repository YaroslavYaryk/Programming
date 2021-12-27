# import random
import time

# def suma(arr):

#     if len(arr) == 0:
#         return 0
#     else:
#         return arr[0] + suma(arr[1:])


# arr = [1, 2, 3, 4, 54, 3, 2, 1, 3, 1, 4]
# print(suma(arr))


# def main(arr):
#     storage = 0
#     for i in arr:
#         storage += i
#     return storage


# print(main(arr))


# def counter(arr):

#     if arr == []:
#         return 0
#     else:

#         return 1 + counter(arr[1:])


# arr = [1, 2, 3, 4, 54, 3, 2, 1, 3, 1, 4]
# print(counter(arr))


# def max(list):
#     if len(list) == 2:
#         return list[0] if list[0] > list[1] else list[1]
#     sub_max = max(list[1:])
#     return list[0] if list[0] > sub_max else sub_max


# arr = [1, 2, 3, 4, 54, 3, 2, 1, 3, 1, 4]
# print(max(arr))


# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:

#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)


# print(quicksort([10, 5, 2, 3, 11, 23, 34, 32, 11, 1, 2]))


# def quicksort(nums):
#     if len(nums) <= 1:
#         return nums
#     else:
#         q = random.choice(nums)
#         s_nums = []
#         m_nums = []
#         e_nums = []
#         for n in nums:
#             if n < q:
#                 s_nums.append(n)
#             elif n > q:
#                 m_nums.append(n)
#             else:
#                 e_nums.append(n)
#         return quicksort(s_nums) + e_nums + quicksort(m_nums)


# print(quicksort([10, 5, 2, 3, 11, 23, 34, 32, 11, 1, 2]))


# def paranoi(s):
#     if len(s) == 1:
#         return True
#     if s[0] != s[-1]:
#         return False
#     else:
#         return paranoi(s[1:-1])


# def Main(s):
#     if paranoi(s):
#         return "Polindrom"
#     else:
#         return "No"


# print(Main("m"))
def timer(funk):
  
    start = time.time()
    def wrapper(*args, **kwargs):
        
        result = funk(*args, **kwargs)
        return result
        
    print(time.time() - start)    

    return wrapper

# @timer
def Fib(n):
    Fib = [0, 1] + [0] * (n - 1)
    for i in range(2,n+1):
        Fib[i] = Fib[i-1] + Fib[i - 2]
    return Fib[n]    

print(Fib(70))    

# @timer
# def Fibo(n):
#     return Fibo(n-1) + Fibo(n-2) if n > 1 else n

# print(Fibo(40))    


# def count_trajectories(n, allowed:list):
#     k = [0, 1] + [0] * (n - 3)
#     for i in range(3, n + 1):
#         if i in allowed:
#             k[i] = k[i-1] + k[i-2] + k[i-3]
#     return k[n]        

# print(count_trajectories(5, [2,3,4,5]))