# 3 кортежа целых чисел. Найти елементы, которые есть во всех кортежах
# 
import random
tuple_1 = tuple(random.randint(0, 10) for i in range(10))
tuple_2 = tuple(random.randint(0, 10) for i in range(10))
tuple_3 = tuple(random.randint(0, 10) for i in range(10))
print('Tuple 1 :', tuple_1, '\n', 'Tuple 2 :', tuple_2, '\n', 'Tuple 3 :', tuple_3, '\n',)
result=set(tuple_1) & set(tuple_2) & set(tuple_3)
print('Common elements in three tuples :')
if len(result)==0:
    print('There are no common elements.', '\n')
else:
    print(tuple(result))
    print(*result, sep=', ')
    print()

# 3 кортежа. Найти уникальные значения для каждого кортежа.
# 
# import random
# tuple_1 = [random.randint(0, 10) for i in range(10)]
# tuple_2 = [random.randint(0, 10) for i in range(10)]
# tuple_3 = [random.randint(0, 10) for i in range(10)]
# print('Tuple 1 :', tuple_1, '\n', 'Tuple 2 :', tuple_2, '\n', 'Tuple 3 :', tuple_3, '\n',)
# uniq_1= tuple(i for i in tuple_1 if tuple_1.count(i)==1)
# print('Tuple 1 :', uniq_1)
# uniq_2= tuple(i for i in tuple_2 if tuple_2.count(i)==1)
# print('Tuple 1 :', uniq_2)
# uniq_3= tuple(i for i in tuple_3 if tuple_3.count(i)==1)
# print('Tuple 3 :', uniq_3)



# 3 кортежа. Найти одинаковые елементы на той-же позиции.
# import random
# tuple_1 = tuple([random.randint(0, 10) for i in range(10)])
# print(tuple_1)
# tuple_2 = tuple([random.randint(0, 10) for i in range(10)])
# print(tuple_2)
# tuple_3 = tuple([random.randint(0, 10) for i in range(10)])
# print(tuple_3)
# print('Match in exact place and meaning :', '\n')
# counter=0
# for i in range(10):
#     if tuple_1[i]==tuple_2[i]==tuple_3[i]:
#         counter+=1
#         print(tuple_1[i])
# if counter==0:
#     print('Match not found')