# # Первая запись позволяет пройти по всем елементам данных с помощью цикла
# for i in user_data:
#     filtered_user_data.append(i)

# # Эта запись равноценна первой
# filtered_user_data=[i for i in user_data]

# Минимум из ряда чисел
# Определяем функцию, в аргументе - список чисел
# def minimum(elements: list) ->int:
# Меняем в аргументена args и kwargs
# def minimum(*args, **kwargs) ->int:
#     # print('-->', elements)
#     print('-->', args)
#     print('-->', kwargs)
#     # return min(elements)
#     return min(args)

# # Вводим произвольное значение чисел и символов
# user_data=input('Enter number: ').split()
# # Получаем список из цифр, все остальное отбрасывается
# filtered_user_data=[int(i) for i in user_data if i.isdigit()]
# # Печатаем список
# # print(filtered_user_data)
# # Печатаем распакованый список
# # print(*filtered_user_data)
# # Передаем список в аргумент функцию и рспаковываем ее
# result=minimum(*filtered_user_data)
# print('result is: ', result)

# def foo(a: int, *args, **kwargs)->int:
#     print('-->', args)
#     print('-->', kwargs)
#     return a+1

# a=foo(2, 3, 2, name='Hello')
# print(a)

# def beautiful_print(*args,**kwargs)->None:
#     # print('-->', kwargs)
#     body=''
#     for key, value in kwargs.items():
#         print(f'{key:10} {value}')
#         # print('-->', key)
#         # print('-->', value)

# data={
#     'name': 'Dima',
#     'age': 29,
#     'height': 190
# }

# # print(data)
# beautiful_print(**data)

# IF/ELSE
# TRY/EXCEPT

# a=input('Enter data: ')
# if a.isdigit():
#     a=int(a)
#     print(a)

# a=input('Enter data: ')
# try:
#     a=int(a)
#     print('A:', a)
# except ValueError:
#     print('Not valid')

# Формат записи с главной функцией по принципу языка Си

# def my_max(*args) -> int:
#     return max(*args)

# def my_min(*args) -> int:
#     return min(*args)

# def main():
#     a=input('Enter data:')
#     mmin=my_min(a)
#     mmax=my_max(a)
#     print(mmin)
#     print(mmax)
#     print(a)

# main()

# Формат записи с главной функцией в Питоне

# def my_max(*args) -> int:
#     return max(*args)

# def my_min(*args) -> int:
#     return min(*args)

# if __name__=='__main__':
#     a=input('Enter data:')
#     mmin=my_min(a)
#     mmax=my_max(a)
#     print(locals())
#     print(mmin)
#     print(mmax)
#     print(a)

# Работа с файлами в Питоне
# C:\dir\file
#  /dir/file
# print('\\')

# File stream
# File='message.txt'
# stream=open(File, mode='r', encoding=None)
# stream=open(File, mode='w', encoding=None)
# stream=open(File, mode='a', encoding=None)
# stream=open(File, mode='r+', encoding=None)
# stream=open(File, mode='w+', encoding=None)

# stream=open(r'C:\Users\Lenovo\Code\Skillup_course\initial_file.txt')

File='initial_file.txt'

# try:
#     stream=open(r'C:\Users\Lenovo\Code\Skillup_course\initial_file.txt')
#     # stream=open(File)
#     line=stream.readlines()
#     print(line)
#     stream.close()

# except FileNotFoundError:
#     print('File not found')

def read_from_file(filename: str) -> list:
    try:
        stream=open(r'C:\Users\Lenovo\Code\Skillup_course\initial_file.txt')
        line=stream.readlines()
        stream.close()
        return line

    except FileNotFoundError:
        print('File not found')


def write_in_file(filename: str, text: str) -> list:
    try:
        stream=open(r'C:\Users\Lenovo\Code\Skillup_course\initial_file.txt', mode='w')
        stream.write(text)
        stream.close()
        return line

    except FileNotFoundError:
        print('File not found')

def update_in_file(filename: str, text: str):
    try:
        stream=open(r'C:\Users\Lenovo\Code\Skillup_course\initial_file.txt', mode='a')
        stream.write(text)
        stream.close()
        return line

    except FileNotFoundError:
        print('File not found')

# with open(r'C:\Users\Lenovo\Code\Skillup_course\initial_file.txt', mode='a') as f:
#     f.write('Contex manager')

line=read_from_file(filename=File)
print(line)

user_input=input('Enter any data: ')
write_in_file(filename=File, text=user_input)

user_input=input('Update any data: ')
update_in_file(filename=File, text=user_input)

line=read_from_file(filename=File)
print(line)