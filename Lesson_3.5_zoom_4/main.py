# Модули

# from math import pi
# # import math

# # pi=3.14
# # print(pi)
# # print(math.pi)
# # print(math.sin(math.pi/2))

# def sin(x):
#     if 2*x==pi:
#         return 0.99999
#     else:
#         None

# # pi=3.14

# print(sin(pi/2))
# # print(math.sin(math.pi/2))

# from math import (pi as system_pi, 
#                   e as exp, 
#                   sin as sinus)
# # from math import *
# # * - импортировать все

# print(sinus(system_pi/2))

# pi=3.14

# def sin(x):
#     if 2*x==pi:
#         return 0.99999
#     else:
#         None

# print(sin(pi/2))

# Random (0.0: 1.0) - диапазон
# from random import random

# # for i in range(5):
# #     print(random())

# from random import seed

# seed(0)

# for i in range(5):
#     print(random())

# seed(5)

# for i in range(5):
#     print(random())

# from random import randrange, randint

# print(randrange(0,12,2))

# for i in range(10):
#     print(randint(1,10), end=',')

# from random import choice, sample

# # choice(seq)

# # sample(seq, elements_to_choice=1)

# lst=[1,2,3,4,5,6,7,8,9,10]
# print(choice(lst))

# print(sample(lst,5))

# Сведения про ОС
# from platform import platform

# print(platform())
# print(platform(0,1))
# print(platform(aliased=False,terse=False))

# Сведения про железо

# from platform import machine

# print(machine())

# from platform import processor

# print(processor())

# # Опять ОС

# from platform import system

# print(system())

# from platform import version

# print(version())

# from platform import python_version_tuple

# print(python_version_tuple())


# Работа с модулями

# from my_module import PI

# print(PI)

from module import sum1, prod1

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(sum(zeroes))
print(sum(ones))

# print(module.counter)
# print(__name__)
# print(module.__name__)