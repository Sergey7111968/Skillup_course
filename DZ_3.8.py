# Домашнее задание

# Задание 1

# Создайте класс Device, который содержит информацию об устройстве.
# С помощью механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о кофемашине), 
# класс Blender (содержит информацию о блендере), класс MeatGrinder (содержит информацию о мясорубке).
# Каждый из классов должен содержать необходимые для работы методы.

# class Device:
#     def foo(self):
#         print('I am a Device')

# class CoffeeMachine(Device):
#     def foo(self):
#         super().foo()
#         print('I am a CoffeeMachine')

# class Blender(Device):
#     def foo(self):
#         super().foo()
#         print('I am a Blender')

# class MeatGrinder(Device):
#     def foo(self):
#         super().foo()
#         print('I am a MeatGrinder')
        

# print(CoffeeMachine. __mro__)
# CoffeeMachine = CoffeeMachine()
# CoffeeMachine.foo()

# print(Blender. __mro__)
# Blender = Blender()
# Blender.foo()

# print(MeatGrinder. __mro__)
# MeatGrinder = MeatGrinder()
# MeatGrinder.foo()

# Задание 2

# Создайте класс Ship, который содержит информацию о корабле.
# С помощью механизма наследования, реализуйте класс Frigate (содержит информацию о фрегате), 
# класс Destroyer (содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере).
# Каждый из классов должен содержать необходимые для работы методы.

class Ship:
    def __init__(self, purpose = str, displayment = int, crew = int, armament = int, engine = str, max_speed = int):
        self.purpose = purpose
        self.displayment = displayment
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed

    def show_ship_information(self):
        """Show information about ship"""
        print('-------------------------')
        print(f'Назначение: {self.purpose}')
        print(f'Водоизмещение: {self.displayment}')
        print(f'Экипаж: {self.crew} человек')
        print(f'Вооружение: {self.armament}')
        print(f'Двигатель: {self.engine}')
        print(f'Максимальная скорость: {self.max_speed}')
        print('-------------------------')

class Frigate(Ship):
    def __init__(self, name = str, purpose = str, displayment = int, crew = int, armament = int, engine = str, max_speed = int):
        self.name = name
        self.purpose = purpose
        self.displayment = displayment
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed

    def demonstration(self):
        """Show information"""
        print(f'Фрегат {self.name}')
        print('-------------------------')
        print('Тут должно быть определение фрегата')
        super().show_ship_information()

class Destroyer(Ship):
    def __init__(self, name = str, purpose = str, displayment = int, crew = int, armament = int, engine = str, max_speed = int):
        self.name = name
        self.purpose = purpose
        self.displayment = displayment
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed

    def demonstration(self):
        """Show information"""
        print(f'Эсминец {self.name}')
        print('-------------------------')
        print('Тут должно быть определение эсминца')
        super().show_ship_information()

class Cruiser(Ship):
    def __init__(self, name = str, purpose = str, displayment = int, crew = int, armament = int, engine = str, max_speed = int):
        self.name = name
        self.purpose = purpose
        self.displayment = displayment
        self.crew = crew
        self.armament = armament
        self.engine = engine
        self.max_speed = max_speed

    def demonstration(self):
        """Show information"""
        print(f'Крейсер {self.name}')
        print('-------------------------')
        print('Тут должно быть определение крейсера')
        super().show_ship_information()


frigate = Frigate('Лариса', 'Малый корабль', 20000, 131, 10, 'Турбо', 15)
frigate.show_ship_information()
print(frigate.demonstration())

destroyer = Destroyer('Aня', 'Уничтожитель', 30000, 200, 20, 'Дизель', 25)
destroyer.show_ship_information()
print(destroyer.demonstration())

сruiser = Cruiser('Катя', 'Рейдер', 40000, 300, 30, 'Дизель', 35)
сruiser.show_ship_information()
print(сruiser.demonstration())


# Задание 3
# Запрограммируйте класс Money (объект класса оперирует одной валютой) для работы с деньгами.
# В классе должны быть предусмотрены поле для хранения целой части денег 
# (доллары, евро, гривны и т.д.) и поле для хранения копеек (центы, евроценты, копейки и т.д.).
# Реализовать методы для вывода суммы на экран, задания значений для частей.