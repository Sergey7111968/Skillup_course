# def print_text(text):
#     print(text)
# print_text('Some')

# def print_hello():
#     print('hello')
# print_hello()

# Встроенные функции
words=['Welcome', 'to', 'Python']
# words_2=['Welcome', 'to', 'Python']
#print(words, words_2, end='dsfsgghdh')

# word_1='Hello'
# word_2='from'
# word_3='Python'
# print(word_1, word_2, word_3, sep=' !!! ')
# print(word_1, word_2, word_3, sep='\t')
# print(word_1, word_2, word_3, sep='\n')

# print(len(words))

# n=3
# d={'1': 'Hello'}
# print(str(n))
# print(str(words))
# print(str(d))

# print(int('1232'))
# print(float('123'))

# import math
# print(int(math.sqrt(25)))

# from math import sqrt
# print(int(sqrt(25)))

# print(bool(5))
# print(bool(1))
# print(bool(-1))
# print(bool(0))
# print(bool(words))
# print(bool(None))

# words_1=[]
# if not words_1:
#     print('There is no words')

# for index, word in enumerate(words, start=1):
#     print(index, word)

# list_1=[2, 1, 3, 4, 7, 11]
# list_2=['P', 'y', 't', 'h', 'o', 'n', 's']
# list_3=['P', 'y', 't', 'h', 'o', 'n', 's']
# iterable_object=zip(list_2, list_1, list_3)
# print(iterable_object)
# for n, value, k in iterable_object:
#     print(n, value, k)

# reversed(list_2)
# for i in reversed(list_2):
#     print(i)
# a=reversed(list_2)
# print(tuple(a))

# a=[
#     ['key', 'value'], 
#     ['key_2', 'value_2']
# ]
# print(dict(a))

# a=sorted(words)
# #print(sorted(words))
# # print(words)
# words.sort()
# print(words)

# #print(list(reversed(words)))
# # words.reverse()
# # print(words)

# print(sorted(words, reverse=True))

# any, all

# a='казак'
# if a==a[::-1]:
#     print('Yes')
# else:
#     print('No')

# def palindromic(sequence):
#     for n, m in zip(sequence, reversed(sequence)):
#         if n!=m:
#             return False
#     return True

# print(palindromic('asdsa'))
# print(palindromic('asdsasdqwea'))
# print(palindromic('adda'))


# def palindromic(sequence):
#     return not any (
#         n!=m for n, m in zip(sequence, reversed(sequence))
#     )
            
# print(palindromic('asdsa'))
# print(palindromic('asdsasdqwea'))
# print(palindromic('adda'))

# def palindromic(sequence):
#     return all (
#         n==m for n, m in zip(sequence, reversed(sequence))
#     )
            
# print(palindromic('asdsa'))
# print(palindromic('asdsasdqwea'))
# print(palindromic('adda'))

# for i in range(10):
#     breakpoint()
#     print(i)

# print(dir())
