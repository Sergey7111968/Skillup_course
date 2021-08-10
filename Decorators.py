# функция в Питоне

# def hi(name='yasoob'):
#     return "Привет " + name

# print(hi("yasoob"))
# # Вывод: 'Привет yasoob'

# # Мы можем присвоить функцию переменной:
# greet = hi
# # Мы не используем здесь скобки, поскольку наша задача не вызвать функцию,
# # а передать её объект переменной. Теперь попробуем запустить

# print(greet())
# # Вывод: 'Привет yasoob'

# # Посмотрим, что произойдет, если мы удалим ссылку на оригинальную функцию
# del hi
# print(hi())
# # Вывод: NameError

# print(greet())
# # Вывод: 'Привет yasoob'

#  Функция внутри функции

# def hi(name="yasoob"):
#     print("Вы внутри функции hi()")

#     def greet():
#         print( "Вы внутри функции greet()")
#     greet()

#     def welcome():
#         print( "Вы внутри функции welcome()")
#     welcome()
#     print("Вы внутри функции hi()")

# hi()
# # Вывод: Вы внутри функции hi()
# #        Вы внутри функции greet()
# #        Вы внутри функции welcome()
# #        Вы внутри функции hi()

# # Пример демонстрирует, что при вызове hi() вызываются также функции
# # greet() и welcome(). Кроме того, две последние функции недоступны
# # извне hi():

# greet()
# # Вывод: NameError: name 'greet' is not defined

# Возвращение функции из функции
# def hi(name="yasoob"):
#     print(name)
#     def greet():
#         return "Вы внутри функции greet()"

#     def welcome():
#         return "Вы внутри функции welcome()"

#     if name == "yasoob":
#         return greet
#     else:
#         return welcome

# a = hi()
# print(a())
# # Вывод: <function greet at 0x7f2143c01500>

# # Это наглядно демонстрирует, что переменная `a` теперь указывает на
# # функцию greet() в функции hi(). Теперь попробуйте вот это

# print(a())

# Передаем функцию в качестве аргумента другой функции
# def hi():
#     return "Привет yasoob!"

# def doSomethingBeforeHi(func):
#     print(func())
#     print("Я делаю что-то скучное перед исполнением hi()")
#     print(func())

# doSomethingBeforeHi(hi)

# Вывод: Я делаю что-то скучное перед исполнением hi()
#        Привет yasoob!

# Декоратор

def a_new_decorator(a_func):

    def wrapTheFunction():
        print("Я делаю что-то скучное перед исполнением a_func()")

        a_func()

        print("Я делаю что-то скучное после исполнения a_func()")

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("Я функция, которая требует декорации")

# a_function_requiring_decoration()
# Вывод: "Я функция, которая требует декорации"

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# Теперь функция a_function_requiring_decoration обернута в wrapTheFunction()

a_function_requiring_decoration()
# Вывод: Я делаю что-то скучное перед исполнением a_func()
#        Я функция, которая требует декорации
#        Я делаю что-то скучное после исполнения a_func()