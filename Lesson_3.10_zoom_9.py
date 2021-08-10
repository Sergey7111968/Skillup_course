# class Myclass:
#     __slots__ = ['a', 'b']

#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        
# m = Myclass(10, 20)
# print(m.a)
# print(m.b)
# m.c = 30
# print(m.c)

#Полиморфизм
# class T1:
#     n = 10
#     def total(self, N):
#         self.total = int(self.n) + int(N)

# class T2:
#     def total(self, s):
#         self.total = len(str(s))
        
# t1 = T1()
# t2 = T2()
# t1.total(45)
# t2.total(45)
# print(t1.total)
# print(t2.total)

# class One:
#     def __init__(self, a):
#         self.a = a**2
# class Two:
#     def __init__(self, a):
#         self.a = a * 2
        
# a = int(input('Enter a number: '))

# if -100 < a < 100:
#     obj = One(a)
# else:
#     obj = Two(a)

# print(obj.a)

# class Sample:
#     def __new__(cls, **kwargs):
#         pass
#     def __init__(self, **kwargs):
#         pass
#     def __del__(self):
#         pass

# class A:
#     @staticmethod
#     def __init__():
#         pass

# a = A()
# a.x = 20
# print(a.x)

# a = 10
# b = 20
# print(a>b)
# print(type(type(a)))
# print(type(a))

# Специальные (магические) методы
# class A:
#     def __init__(self, x):
#         self.x = x
#     def __eq__(self, other):
#         return self.x == other.x
#     def __add__(self, other):
#         return self.x + other.x
            

# a = A(20)
# b = A(20)

# print(a == b)
# print(a + b)

# 3x^2 + 4X + 7
# 2x^2 + 2X + 7

# class Polynom:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def __add__(self, other):
#         pass
            

# poly_1 = Polynom(2, 5, 8)
# poly_2 = Polynom(1, 2, 3)
# print(poly_1 + poly_2)

#Функторы
# s = 'www.example.com'
# print(s.strip('w.com'))

# class Strip:
#     def __init__(self, character):
#         self.character = character
#     def __call__(self, string):
#         return string.strip(self.character)

# site_strip = Strip('w.com')
# print(site_strip(s))

# def make_strip_function(character):
#     def strip_func(string):
#         return string.strip(character)
#     return strip_func

# site_strip = make_strip_function('w.com')
# print(site_strip(s))

class SortKey:
    def __init__(self, *kwargs):
        self.attrs = kwargs
    def __call__(self, instance):
        values = []
        for attr in self.attrs:
            values.append(getattr(instance, attr))
        return values

class Person:
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email

    def __repr__(self):
        return self.name

joe = Person('Joe', "QWE", 'joe@mail.com')
mark = Person('Mark', "QWasdE", 'mark@mail.com')
jack = Person('Jack', "Q123WqweqeE", 'jack@mail.com')
people = [joe, mark, jack]
print(people)
print(people.sort(key = SortKey('name')))

# l = ['gftdrsesaerd', 'tre']
# print(sorted(l, key = len))
# print(sorted(l))

# class Foo:
#     def __init__(self):
#         self.bar = 'hello'

# foo = Foo()
# print(foo.bar)

# class Temperature:
#     def __init__(self, celcius):
#         self._celcius = celcius

#     @property
#     def celcius(self):
#         return self._celcius

#     @celcius.setter
#     def celcius(self, value):
#         self._calcius = value

#     @property
#     def kelvins(self):
#         return self.celcius + 273

# t = Temperature(20)
# print(t.celcius)
# print(t.kelvins)
# t.celcius = 30
# print(t.celcius)
# print(t.kelvins)


