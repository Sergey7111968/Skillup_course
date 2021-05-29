# Форматированный текст

# def format():
#     text='''"Don't compare yourself with anyone in this world...\nif you do so, you are insulting yourself."\n\t\t\t\t\t\t\tBill Gates'''
#     print(text)

# format()

# Четные числа

# print('Enter two number through space:')
# number_1, number_2=map(int,input().split())

# def even():
#     for i in range(number_1, number_2+1):
#         if i%2==0:

#             print(i, end = " ")

# even()

# Заполненный квадрат

# print('Enter length :')
# length=int(input())
# print('Enter simbol :')
# simbol=input()
# print('Enter type_bool :')
# type_bool=(input())
# print(type_bool)

# def hollow_square():
#     if type_bool=='True':
#         for i in range(0,length):
#             print(length*simbol)

#     elif type_bool=='False':
#         print (simbol*length)
#         for i in range(2,length):
#                 print ('{0} {1} {0}'.format(simbol, " "*(length-4)))
#         print (simbol*length)

# hollow_square()

# Минимум из пяти чисел

# print('Enter five number through space:')
# number_1, number_2, number_3, number_4, number_5=map(int,input().split())

# def min_five():
#     print(min(number_1, number_2, number_3, number_4, number_5))


# min_five()

# Произведение чисел в диапазоне

# def multiply():
#     print('Enter two number through space:')
#     number_1, number_2=map(int,input().split())
#     mult=1
    
#     if number_1>number_2:
#         number_1, number_2=number_2, number_1
        
#     for i in range(number_1, number_2+1):
#         mult*=i
#     print(mult)

# multiply()

# Количество цифр в числе

# def count_number():
#     print('Enter number :')
#     number=input()
#     print(len(number))
        
# count_number()

# Палидром

def palindrom():
    print('is the number a palindrome? Enter number :')
    number=input()
    if number[:]==number[::-1]:
        print('True')
    else:
        print('False')

palindrom()

