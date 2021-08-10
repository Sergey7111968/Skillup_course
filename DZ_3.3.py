# Функция-декоратор, которая возводит в квадрат значение, которое возвращает функция, к которой применяется декоратор

# def param_transfer(func):
#    def wrapper(arg):
#        print("Run function: " + str(func.__name__) +" with param: " + str(arg))
#        print(func(arg**2))
#    return wrapper

# @param_transfer
# def print_square(arg):
#   return arg

# # print_square = param_transfer(print_square)
# print_square(6)

# Второй вариант этой функции

def decor_square(fun):
  def inner(n):
    fun(n)
    print(f'Квадрат числа {n} равняется {n**2}.')
  return inner

# @decor_square
# def my_func(n:int):
#   return n

# n=int(input('Введите число: '))

# my_func(n)

# Декоратор подключения драйвера к принтеру
# def driver_connection(*arguments)
# @driver_connection
# def hp_printer(*attributes)

# print('\nTasks2')

# from random import choice

# def driver_connection(func):
#   def wrapper(*args):
#     func(*args)
#     print(f'Автор документа: {a} \n')

#   return wrapper

# @driver_connection
# def hp_printer(a):
#   print('Напечтано на HP')

  
# a=choice (['Ионов', 'Шевченко', 'Мельник'])

# hp_printer(a)

  
