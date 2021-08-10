# Задание №1
# Написать маленькую программу, которая на Ваше усмотрение,
# реализует полиморфизм. Пример придумать самим

# class Young:
#     def __init__(self, year):
#         self.year = year
#         print ('Young man')
# class Old:
#     def __init__(self, year):
#         self.year = year
#         print('Old man')
        
# year = int(input('Enter an age: '))

# if 10 <= year <= 50:
#     obj =Young(year)
# else:
#     obj = Old(year)

# print(obj.year)

# Задание №2

# Реализовать клас Температуры (как сегодня в конце урока), 
# который на основе @property будет возвращать, присваивать данные для цельсиев, фаренгейтов и кельвинов.

# class Temperature:
#     def __init__(self, celcius):
#         self.__celcius = celcius

#     @property
#     def celcius(self):
#         return self.__celcius

#     @celcius.setter
#     def celcius(self, value):
#         self.__calcius = value

#     @property
#     def kelvins(self):
#         return self.__celcius + 273

#     @property
#     def farengaits(self):
#         return int(self.__celcius * 1.8 + 32)

# t = Temperature(20)
# print(f'Температура в цельсиях: {t.celcius}')
# print(f'Температура в кельвинах: {t.kelvins}')
# print(f'Температура в фаренгейтах: {t.farengaits}')
# t.celcius = 22
# print(f'Температура в цельсиях: {t.celcius}')
# print(f'Температура в кельвинах: {t.kelvins}')
# print(f'Температура в фаренгейтах: {t.farengaits}')

# class Temperature:
#     def __init__(self, mark = int, scale = str):
#         self.__mark = mark
#         self.__scale = scale

#     @property
#     def celcius(self):
#         if self.__scale == 'C':
#             return self.__mark
#         if self.__scale == 'F':
#             return (self.__mark - 32) *(5/9)
#         if self.__scale == 'K':
#             return int(self.__mark - 273.15)

#     @celcius.setter
#     def celcius(self, value):
#         self.__mark = value
#         self.__scale = 'C'

#     @property
#     def fahrenheit(self):
#         if self.__scale == 'C':
#             return int(self.__mark  * 1.8 + 32)
#         if self.__scale == 'F':
#             return self.__mark 
#         if self.__scale == 'K':
#             return int((self.__mark - 273.15) * (9/5) + 32)

#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.__mark = value
#         self.__scale = 'F'

#     @property
#     def kelvin(self):
#         if self.__scale == 'C':
#             return int(self.__mark + 273.15)
#         if self.__scale == 'F':
#             return int((self.__mark - 32) * (5/9) + 273.15) 
#         if self.__scale == 'K':
#             return self.__mark 

#     @fahrenheit.setter
#     def fahrenheit(self, value):
#         self.__mark = value
#         self.__scale = 'K'

# t = Temperature(20, 'F')
# print(f'Температура в цельсиях: {t.celcius}')
# print(f'Температура в кельвинах: {t.kelvin}')
# print(f'Температура в фаренгейтах: {t.fahrenheit}')
# t.fahrenheit = 20
# print(f'Температура в цельсиях: {t.celcius}')
# print(f'Температура в кельвинах: {t.kelvin}')
# print(f'Температура в фаренгейтах: {t.fahrenheit}')

# Задание №3

# Бонус+ режим: кто сможет закончить пример с ФУНКТОРОМ сортировки 
# ч-з класс получит от меня мастеркласс по чистой архитектуре кода, когда будем изучать ВЕБ )

class SortKey:
    values = []

    def __init__(self, *kwargs):
        self.attrs = kwargs
    
    def __call__(self, instance):
        for attr in self.attrs:
            self.values.append(getattr(instance, attr))
            self.values = [str(i) for i in self.values]
            self.values.sort()
            return self.values
            # Да, способ топорный, но работает

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
people.sort(key = SortKey('email'))
print(people)
people.sort(key = SortKey('surname'))
print(people)
