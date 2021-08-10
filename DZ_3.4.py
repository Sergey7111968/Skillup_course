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

# !!!Второй вариант решения задачи!!!

# def file_match():
#     with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as file1, open (r'C:\Users\Lenovo\Code\Skillup_course\message_2.txt') as file2:
#         line_1=file1.readlines()
#         line_2=file2.readlines()

         
#         if line_1==line_2:
#             print('Файлы совпадают')

#         else:
#             print('В файлах не совпадают следующие строки: ')
#             list1=[i for i in line_1 if i not in line_2 and i!='\n']
#             list2=[c for c in line_2 if c not in line_1 and c!='\n']
#             print(''.join(list1 + list2), end='')

# file_match()


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

# Задача №3
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

# !!!Второй вариант решения задачи!!!
# def statistics():
#     try:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as stream, open(r'C:\Users\Lenovo\Code\Skillup_course\message_3.txt', mode='w') as result:
#             lines=stream.readlines()
#             print(lines)
#             line=("".join(lines)).replace('\n', '').replace(' ', '')
#             print(line)
#             vowels=['A', 'E', 'I', 'O', 'U', 'Y']
#             vowels_in_line=[i for i in line.upper() if i in vowels]
#             digits_in_line=[i for i in line if i.isdigit()]
#             consonants_in_line=[i for i in line.upper() if i not in vowels and i not in digits_in_line and i!='']
#             result.write(f'Количество строк: {len(lines)}\n')
#             result.write(f'Обще количество символов: {len(line)}\n')
#             result.write(f'Обще количество гласных: {len(vowels_in_line)}\n')
#             result.write(f'Обще количество согласных: {len(consonants_in_line)}\n')
#             result.write(f'Обще количество цифр: {len(digits_in_line)}\n')

#     except FileNotFoundError:
#         print('File not found')

# statistics()

# Задача №3
# !!!Дан текстовый файл. Удалить из него последнюю строку!!!
# Результат записать в другой файл

# def delete_last():
#     try:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as stream, open(r'C:\Users\Lenovo\Code\Skillup_course\message_4.txt', mode='w') as result:
#             lines=stream.readlines()
#             result.write(''.join(lines[:-1]))

#     except FileNotFoundError:
#         print('File not found')

# delete_last()

# Задача №4
# Найти длину самой длинной строки

# def read_from_file_1(filename: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.readlines()
#             length_str=[]
#             for i in range(len(word)):
#                 length_str.append(len(word[i]))
#             print(max(length_str))

      
# read_from_file_1(filename=File_1)


# !!!Второй вариант задачи №4!!!

# def maximal_line():
#     try:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as stream:
#             list1=[]
#             for i in stream:
#                 list1.append(len(i.replace("\n",'')))
#             print(f'Максимальная длина строки: {max(list1)} символ(a)')

#     except FileNotFoundError:
#         print('File not found')

# maximal_line()


# Задача №5
# Сколько раз встречается заданное пользователем слово
    

# def read_from_file_1(filename: str, text: str) -> list:
#         with open(r'C:\Users\Lenovo\Code\Skillup_course\message_1.txt') as f:
#             word=f.read()
#             word=word.count(text)
#             return word
                             
# user_input=input('Enter any word: ')
# line_1=read_from_file_1(filename=File_1, text=user_input)
# print(line_1)

# Задача №6
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
