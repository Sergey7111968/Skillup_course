File_1='message_1.txt'
File_2='message_2.txt'
File_3='message_3.txt'

# Задача №1
# Есть два тектовых файла, выяснить, совпадают ли их строки
# Если нет - выводим несовпадающую строку каждого из файлов

# def read_from_file_1(filename: str)->list:
    
#     try:
#         stream=open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt')
#         line=stream.readlines()
#         stream.close()
#         return line

#     except FileNotFoundError:
#         print('File not found')

# line_1=read_from_file_1(filename=File_1)
# print(line_1)


# def read_from_file_2(filename: str) -> list:
    
#     try:
#         stream=open(r'C:\Users\Lenovo\Code\Skillup_course\message_2.txt')
#         line=stream.readlines()
#         stream.close()
#         return line

#     except FileNotFoundError:
#         print('File not found')

# line_2=read_from_file_2(filename=File_2)
# # print(line_2)

# if line_1!=line_2:
#     print(line_1)
#     print(line_2)

# else:
#     print('Strings match')

# Задача №2
# Дан текстовый файл. Создать новый файл и записать в нем статистику:
# количество символов, количество строк, количество гласных букв, 
# коичество согласных букв, количество цифр

# Количество символов
# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             number_simbol=len(f.read())
#             return number_simbol
                                    
# number_simbol=read_from_file_1(filename=File_1)
# print(number_simbol)


# # Количество строк
# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             number_string=len(f.readlines())
#             return number_string
                                    
# number_string=read_from_file_1(filename=File_1)
# print(number_string)

# # Количество гласных букв
# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.read()
#             # vowels=word.count('a')
#             vowels = set("AEIOUYaeiouy")
#             word_set = set(word.lower())
#             vowels=len(word_set.intersection(vowels))
#             return vowels
                        
# vowels=read_from_file_1(filename=File_1)
# print(vowels)

# # Количество согласных букв
# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.read()
#             cons = set("bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ")
#             word_set = set(word.lower())
#             cons=len(word_set.intersection(cons))
#             return cons
            
# cons=read_from_file_1(filename=File_1)
# print(cons)

# # Количество цифр в файле
# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.read()
#             number = set("0123456789")
#             word_set = set(word.lower())
#             number=len(word_set.intersection(number))
#             return number
            

# number=read_from_file_1(filename=File_1)
# print(number)

# def write_in_file(filename: str, text: str) -> list:
#     try:
#         stream=open(r'C:\Users\Lenovo\Code\Skillup_course\message_3.txt', mode='w')
#         line_3=stream.write(text)
#         stream.close()
#         return line_3

#     except FileNotFoundError:
#         print('File not found')

# user_input=number_simbol, number_string, vowels, cons, number
# write_in_file(filename=File_3, text=str(user_input))

# Найти длину самой длинной строки

# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.readlines()
#             return word
                            

# line_1=read_from_file_1(filename=File_1)
# print(line_1)

# length_str=[]
# for i in range(len(line_1)):
#     length_str.append(len(line_1[i]))
# print(max(length_str))

# Сколько раз встречается заданное пользователем слово
    

# def read_from_file_1(filename: str, text: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.read()
#             word=word.count(text)
#             return word
                             
# user_input=input('Enter any word: ')
# line_1=read_from_file_1(filename=File_1, text=user_input)
# print(line_1)

# Найти и заменить заданное пользователем число

# def read_from_file_1(filename: str, text_1: str, text_2: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.read()
#             word=word.replace(text_1, text_2)
#             return word
                             
# user_input_1=input('Enter number one: ')
# user_input_2=input('Enter number two: ')
# line_1=read_from_file_1(filename=File_1, text_1=user_input_1, text_2=user_input_2)
# print(line_1)
