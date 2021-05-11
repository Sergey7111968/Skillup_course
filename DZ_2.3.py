# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# list_2 = [random.randint(0, 10) for i in range(10)]
# list_3 = list_1+list_2
# print(list_3)

# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# list_2 = [random.randint(0, 10) for i in range(10)]
# list_3 = list(set(list_1 + list_2))
# print(list_3)

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

# import random
# list_1 = [random.randint(0, 10) for i in range(10)]
# print(list_1)
# list_2 = [random.randint(0, 10) for i in range(10)]
# print(list_2)
# list_3 = list(set(list_1)) + list(set(list_2))
# print(list_3)

import random
list_1 = [random.randint(0, 10) for i in range(10)]
print(list_1)
list_2 = [random.randint(0, 10) for i in range(10)]
print(list_2)
list_3 = [min(list_1), max(list_1), min(list_2), max(list_2)]
print(list_3)