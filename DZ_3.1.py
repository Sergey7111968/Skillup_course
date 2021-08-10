# 1. Произведение списка целых чисел

import random
list_1 = [random.randint(0, 10) for i in range(10)]
print(list_1)

# def multiply(list_1):
#     mult = 1
#     for i in list_1:
#         mult *= i
#     return mult    
 
# print(multiply(list_1))

# 2. Нахождение минимума списка

# def minimum(list_1):
#     print(min(list_1))

# minimum(list_1)

# 3. Количество простых чисел

# def simple_number(list_1):
#     count=0
#     for num in list_1:
#         if all(num%i!=0 for i in range(2,num)):
#             if num>0:
#                 count+=1
#     print (count)
    
# simple_number(list_1)

# 4. Количество удаленных елементов

# n=int(input('Enter the number :')) 

# def delete_number(list_1):
     
#     count=0
#     for num in list_1:
#         if num==n:
#             list_1.remove(num)
#             count+=1
#     print (count)
    
# delete_number(list_1)

# 5. Сумма списков целых чисел

# import random

# list_2 = [random.randint(0, 10) for i in range(10)]
# print(list_2)

# def sum_list(list_1, list_2):
#     print(list_1+list_2)

# sum_list(list_1, list_2)


# 6. Степень каждого елемента

n=int(input('Enter the degree :'))
list_3=[]

def degree(list_1, n):
    for i in list_1:
         i=i**n
         list_3.append(i)
    print(list_3)
       
degree(list_1, n)

    







       


            
          

