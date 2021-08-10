# Написать функцию date, принимающую 3 аргумента — день, месяц и год. Вернуть True, если такая дата есть в нашем календаре, и False иначе.
# 
# import datetime
# day=int(input("Введите день :"))# предположим - 29
# month=int(input("Введите месяц :"))# предположим - 2
# year=int(input("Введите год :"))# предположим - 2020

# def date():
#     try:
#         data=datetime.date(year,month,day)
#         print(data)
#         print("Дата существующая")
#     except:
#         print("Такой даты нет")

# date()

# Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно зашифровать,
# и ключ шифрования, которая возвращает строку, зашифрованную путем применения функции XOR (^) над символами строки с ключом.
# Написать также функцию XOR_uncipher, которая по зашифрованной строке и ключу восстанавливает исходную строку.

import itertools


def XOR_cipher(string, key):

    answer = []

    key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)


print(XOR_cipher('Kravchenko', '321'))

# Функция для расшифровки точно такая же (XOR_uncipher = XOR_cipher)

# def is_year_leap(year):

#     if year % 400 == 0 :
#         return True

#     if year % 4 == 0 and year % 100 != 0 :
#         return True

#     return False

# print(is_year_leap(2004))
