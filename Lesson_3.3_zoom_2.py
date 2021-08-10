# def add(a,b):
#     """This function returns sum of a and b.
#     Return: int
#     Params:
#     a: int -- first argument
#     b: int -- second argument
#     """
#     return a+b

# add_2=lambda a, b: a+b

# print(add(2, 4))
# print(add_2(3, 7))

# Type hints
# def printfunction(args: list, fun) ->int:
#     for x in args:
#         print(f"f({x})=" , fun(x), sep='')

# printfunction([x for x in range(-2,3)], lambda x: 2 * x**2 -4 * x + 2)

# printfunction([x for x in range(-2,3)], lambda x: 3 * x**2 -4 * x + 5)

# map(function, iterable)
# list_1=[x for x in range(5)]
# list_2=list(map(lambda x: 2**x, list_1))
# print(list_2)
# for x in map(lambda x: x*x, list_2):
#     print(x, end=' ')
# print()

# users=['Dima', 'Oleg', 'Victoria', 'Alex']
# def my_function(user):
#     if len(user)>4:
#         return user
#     else:
#         return " "

# # list_3=list(map(lambda user: user if len(user)>4 else " ", users))
# list_3=list(map(my_function, users))
# print(list_3)

# filter (function, args: iter)
from random import randint, seed

seed()
data=[randint(-10,10) for i in range(5)]
filtered=list(filter(lambda x: x>0 and x%2==0, data))

print(data)
print(filtered)

# def outer(par):
#     loc=par
#     def inner():
#         return loc
#     return inner

# var=1
# fun=outer(var)

# print(fun())


# def mul(a):
#         def helper(b):
#             return a * b
#         return helper

# new_mul5=mul(5)
# print(new_mul5(2))

# def makeclouser(par):
#     def power(p):
#         return p**par
#     return power

# fsqr=makeclouser(2)
# fcub=makeclouser(3)
# for i in range(5):
#     print(i, fsqr(i), fcub(i))

# def foo(a):
#     if a<0:
#         return
#     print('a =', a)
#     return foo(a=a-1)

# foo(10)

# def fib(n):
#     if n<2:
#         return n
#     return fib(n-2)+fib(n-1)

# print(f'fib(1)={fib(1)}')

# _fib_cache= {
#     1: 1,
#     2: 1,
#     3: 2,
#     4: 3,
#     5: 5,
#     6: 8
# }

# def fib(n):
#     result=_fib_cache.get(n)
#     if not result:
#         result=fib(n-2)+fib(n-1)
#         _fib_cache[n]=result
#     return result 

# print(f'fib(200)={fib(200)}')

# from functools import lru_cache

# @lru_cache
# def fib(n):
#     if n<2:
#         return n
#     return fib(n-2)+fib(n-1)

# print(f'fib(200)={fib(200)}')

# decorators

# def decorator_function(func):
#     def wrapper():
#         print('Function wrapper')
#         func()
#         print('Function wrapper')
#     return wrapper

# @decorator_function
# def hello_world():
#     print('Hello world')

# hello_world=decorator_function(hello_world)
# hello_world()

# def benchmark(func):
#     import time

#     def wrapper():
#         start=time.time()
#         func()
#         end=time.time()
#         print(f'Time of applicationexecuting: {end-start}')
#     return wrapper

# @benchmark
# def fetch_webpage():
#     import requests

#     webpage=requests.get('https://google.com')

# fetch_webpage()

# def benchmark(iters):
#     def actual_decorator(func):
#         import time

#         def wrapper(*args, **kwargs):
#             total=0
#             for i in range(iters):
#                 start=time.time()
#                 return_value=func(*args, **kwargs)
#                 end=time.time()
#                 total=total+(end-start)
#             print(f'Avarage: {total/iters}')
#             return return_value
#         return wrapper
#     return actual_decorator

# @benchmark(iters=10)
# def fetch_google(url: str):
#     import requests
#     webpage=requests.get(url)
#     return webpage.text

# google=fetch_google('https://google.com')
# print(google)
                
