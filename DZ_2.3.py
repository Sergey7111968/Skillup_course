# Два списка случайных чисел в один
#
# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# list_2 = [random.randint(0, 10) for i in range(10)]
# list_3 = list_1+list_2
# print(list_3)

# Елементы обоих списков без повторений
# 
# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# list_2 = [random.randint(0, 10) for i in range(10)]
# list_3 = list(set(list_1 + list_2))
# print(list_3)

# Елементы, общие для двух списков
# 
# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# print(list_1)
# list_2 = [random.randint(0, 10) for i in range(10)]
# print(list_2)
# list_3=[]
# for i in list_1:
#     if i in list_3:
#         continue
#     for j in list_2:
#         if i == j:
#             list_3.append(i)
#             break
# print(list_3)

# Уникальные елементы каждого из списков
# 
import random
list_1 = [random.randint(0, 10) for i in range(10)]
print(list_1)
list_2 = [random.randint(0, 10) for i in range(10)]
print(list_2)
uniq_1=list(i for i in list_1 if list_1.count(i)==1)
uniq_2=list(i for i in list_2 if list_2.count(i)==1)
print('List_1 :', uniq_1)
print('List_2 :', uniq_2)

# Список из минимальных и максимальных значений каждого из списков
# 
# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# print(list_1)
# list_2 = [random.randint(0, 10) for i in range(10)]
# print(list_2)
# # list_3 = [min(list_1), max(list_1), min(list_2), max(list_2)]
# print('Min list_1 :', min(list_1), '\n','Max list_1 :', max(list_1), '\n','Min list_2 :', min(list_2), '\n','Max list_2 :', max(list_2))