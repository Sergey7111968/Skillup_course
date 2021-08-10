# print(type(12))

# open()

# print(repr('123'))

# print(issubclass(int, bool))
# print(issubclass(bool, int))

# print(isinstance(True, int))
# print(isinstance(123, int))

# hasattr
# getattr
# setattr
# delattr

# @classmethod
# @staticmethod

# print(ord('1'))
# print(ord('A'))

# print(chr(65))

# name='Dima'
# surname='Surname'
# a='hello {0} {1} {0}'.format(name, surname)
# a_2=f'hello {name} {surname}' 
# print(a)
# print(a_2)

# LEGB

# y=x^2
def y(x):
    return x**2

print(y(0))
print(y(1))
print(y(2))
print(y(-1))
print(y(-2))

# x=10
# import module from module
# def func():
# def fuct(arg_1, arg_2)
# class MyClass:


# i=100
# a=10
# for i in range(a):
#     print(i)
    
# print(i)

# arg_1='Another text'

# def foo(arg_1):
#     print(arg_1)

# foo(arg_1='hello')

# print(arg_1)

# a='Another text'
# print(id(a))
# def foo(a):
#     print(id(a))
#     print(a)

# foo(a='hello')

# print(a)
# print(id(a))

# def foo():
#     def bar():
#         print('Bar')
#     bar()
#     print('Foo')

# foo()

# h=29
# def foo(a, b):
#     # print(locals())
#     print(globals())
#     # print(h)
#     return a+b

# a=foo(1, 2)
# b=foo(3, 4)

# c=foo(a, b)
# print(a)

# h='asddfddsa'
# def foo(a, b):
#     # print(locals())
#     print(globals())
#     return a+b

# a=foo(1, 2)

# def outer_func():
#     var=100 # Non local variable

#     def inner_func():
#         # Local scope
#         print(f'Printing var from inner_func : {var}')
#     print(locals())
#     inner_func()
#     # print(f'Printing var from inner_func : {var}')

# outer_func()

# const=10

# def increment():
#     global const
#     const+=1

# def increment_2():
#     global const
#     const+=2

# increment()
# increment_2()

# print(const)

# def foo():
#     var=100

#     def bar():
#         nonlocal var
#         var+=100
    
#     bar()
#     print(var)

# foo()

# def power_factory(exp):
#     def power(base):
#         return base**exp
#     return power 

# square=power_factory(2)
# cube=power_factory(3)

# print(square(3))
# print(square(5))

# print(cube(2))
# print(cube(5))

# def power_factory(trigger):
#     def foo():
#         return 10
#     def foo_2():
#         return 12

#     if trigger:
#         return foo
#     return foo_2

# a=power_factory(True)
# print(a())

