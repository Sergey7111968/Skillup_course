# class Animal:
#     age=10

#     def get_age(self):
#         return Animal.age

# animal=Animal()
# print(animal.get_age())

# # Это то же самое, что запись сверху
# animal = {'age' : 10}
# print(animal['age'])

# class Person:
#     def say_hi(self):
#         print('Hi. How are you?')

# p = Person()
# p.say_hi()

# class Person:
#     def __init__(self, name,age, hands, sex):
#         self.name = name
#         self.age = age
#         self.hands = hands
#         self.sex = sex

#     def cleanup(self):
#         if self.sex:
#             print(f'{self.name} начал уборку со стола ')
#         else:
#             print(f'{self.name} начала уборку со стола ')
    
# dima = Person(name='Dima', age=30, hands=True, sex=True)
# sveta = Person(name='Sveta', age=20, hands=True, sex=False)

# dima.cleanup()
# sveta.cleanup()

# print(dima.age)
# print(sveta.age)

# class Robot:
#     """Представляет робота с именем"""
#     # Переменная, которая содержит количество роботов
#     population = 0

#     def __init__(self, name):
#         """Инициализация данных"""
#         self.name=name
#         print(f'Инициализация {self.name}')
#         # Увеличение численности роботов
#         Robot.population += 1

#     def __del__(self):
#         """Деструктор"""
#         print(f'Уничтожение {self.name}')
#         Robot.population -= 1
#         if Robot.population == 0:
#             print(f'{self.name} был последним роботом')
#         else:
#             print(f'Осталось {Robot.population} роботов')

#     def say_hi(self):
#         """Приветствие роботов"""
#         print(f'Привет, меня зовут {self.name}')

#     @staticmethod
#     def how_many():
#         """Выводит численность роботов"""
#         print(f'У нас тут {Robot.population} роботов')

# # droid1 = Robot('R2-D2')
# # droid1.say_hi()
# # # droid1.how_many()
# # Robot.how_many()

# # droid2 = Robot('C-3PO')
# # droid2.say_hi()
# # # droid2.how_many()
# # Robot.how_many()

# # del droid2
# # del droid1

# if __name__ == '__main__':
#     print('Здесь вы можете создать вашего робота.')
#     robot_name = input('Введите имя робота: ')
#     users_robot = Robot(robot_name)


