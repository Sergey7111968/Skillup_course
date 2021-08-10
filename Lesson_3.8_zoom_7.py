#  object_in is object_two
# class SampleClass:
#     def __init__(self, val):
#         self.val = val

# ob1 = SampleClass(0)
# ob2 = SampleClass(2)
# ob3 = ob1
# ob3.val += 1

# print(ob1 is ob2)
# print(ob2 is ob3)
# print(ob3 is ob1)
# print(ob1.val, ob2.val, ob3.val)

# str1 = 'Mary had a little '
# str2 = 'Mary had a little lamb'
# str1 += 'lamb'
# print(str1 == str2, str1 is str2)
  
# class Super:
#     def __init__(self, name, capital = True):
#         self.capital = capital
#         self.name = self.get_name()

#     def get_name(self):
#         if self.capital:
#             return self.name.capitalize()
#         return self.name


#     def __str__(self):
#         return f'My name is {self.name}.'

# class Sub(Super):
#     # pass
#     def __init__(self, name):
#         self.name = name
#         # Super. __init__(self, name)
#         super(). __init__(name)

# obj = Sub('andy')
# print(obj)
# print(type(obj))

# class Super:
#     supVar = 1

# class Sub(Super):
#     subVar = 2

# obj = Sub()

# print(obj.subVar)
# print(obj.supVar)

# class Super:
#     def __init__(self):
#         self.supVar = 11

# class Sub(Super):
#     def __init__(self):
#         super(). __init__()
#         self.subVar = 12

# obj = Sub()

# print(obj.subVar)
# print(obj.supVar)

# class Level1:
#     varia1 = 100

#     def __init__(self):
#         self.var1 = 101

#     def fun1(self):
#         return 102

# class Level2(Level1):
#     varia2 = 200

#     def __init__(self):
#         super(). __init__()
#         self.var2 = 201

#     def fun2(self):
#         return 202

# class Level3(Level2):
#     varia3 = 300

#     def __init__(self):
#         super(). __init__()
#         self.var3 = 301

#     def fun3(self):
#         return 302

# obj = Level3()
# print(obj.varia1, obj.var1, obj.fun1())
# print(obj.varia2, obj.var2, obj.fun2())
# print(obj.varia3, obj.var3, obj.fun3())

# class SuperA:
#     varA = 10

#     def funA(self):
#         return 11

# class SuperB:
#     varB = 20

#     def funB(self):
#         return 21

# class Sub(SuperA, SuperB):
#     pass

# obj = Sub()

# print(obj.varA, obj.funA())
# print(obj.varB, obj.funB())

# class Left:
#     var = 'L'
#     var_left = 'LL'

#     def fun(self):
#         return 'left'

# class Right:
#     var = 'R'
#     var_right = 'RR'

#     def fun(self):
#         return 'Right'

# class Sub(Left, Right):
#     pass

# obj = Sub()

# print(obj.var, obj.var_left, obj.var_right, obj.fun())

# class One:
#     def doit(self):
#         print('doit from One')
#     def doanything(self):
#         self.doit()

# class Two(One):
#     def doit(self):
#         print('doit from Two')
    
# one = One()
# two = Two()

# one.doanything()
# two.doanything()

# # MRO -> Method Resolution Order (порядок разрешения методов) использует алгоритм S3
# print(One.__mro__)
# print(Two.__mro__)

# class A:
#     def foo(self):
#         print('I am in A')

# class B(A):
#     def foo(self):
#         print('I am in B1')
#         super().foo()
#         print('I am in B2')

# class C(A):
#     def foo(self):
#         print('I am in C1')
#         super().foo()
#         print('I am in C2')

# class D(B, C):
#     def foo(self):
#         print('I am in D1')
#         super().foo()
#         print('I am in D2')
        

# print(D. __mro__)
# d = D()
# d.foo()


