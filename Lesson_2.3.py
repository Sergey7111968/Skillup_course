# Literals
# Nimbers, Strings, Bools, None

# Collections
# Strings, Lists, Tuples, Sets, Dicts

# var_1=input('Set var :')
# var_2=input('Set var :')
# var_3=input('Set var :')
# var_100=input('Set var :')

# vars=[]

#class_1=[...]

# people=['john', 'Marry', 'Joe', 'Mark']
# print(people[0])
# print(people[-4])
# print(people[1])
# print(people[-3])
# print(people[2])
# print(people[-2])
# print(people[3])
# print(people[-1])
# print(len(people))
# print(people)
# del people[0]
# print(people)

# Function
# result=fuction(arg)
# y=x**2
# f(x)=x**2

# Method
# result=data.method(arg)

# append
# print(people)
# people.append('Ben')
# print(people)

# # insert
# people.insert(2, 'Mike')
# print(people)

# people=[]
# for i in people:
#     print(i)

# my_list=[10, 1, 8, 5]
# total=0
# for i in range(len(my_list)):
#     total=total+my_list[i]
# print(total)

# my_list=[10, 1, 8, 5]
# total=0
# for i in my_list:
#     total=total+i
# print(total)

# a=5
# b=10
# a,b=b,a
# print(a, b)

# people=['john', 'Marry', 'Joe', 'Mark']
# print(people)
# people_2=people
# print(people_2)

# a=10
# b=10
# print(id(a), id(b), id(10))

# a=['John', 'Mary']
# b=['John', 'Mary']
# print(id(a), id(b))
# print(a==b)

# a=['John', 'Mary']
# b=a
# b.append('Ben')
# print(id(a), id(b))
# print(a)
# print(b)

# a=['John', 'Mary']
# # b=a.copy()
# b=a[::]
# b.append('Ben')
# print(id(a), id(b))
# print(a)
# print(b)

# a=['john', 'Marry', 'Joe', 'Mark']
# print(a[1::-1])

# a=[]
# for element in range(10):
#     a.append(element)
# print(a)

# row=[]
# white_pawn='p'
# # for i in range(8):
# #     row.append(white_pawn)
# row=[white_pawn for i in range(8)]
# print(row)

# squares=[x**2 for x in range(10)]
# print(squares)

# row=[]
# empty='N'
# column=[]
# for i in range(8):
#         for j in range(8):
#             column.append(empty)
#         row.append(column)
#         column=[]
# row[2][2] ='white_pawn'
# print(row)

# from pprint import pprint
# empty='N'
# board=[[empty for i in range(8)] for j in range(8)]
# board[0][0] ='ROOK'
# board[0][7] ='ROOK'
# board[7][0] ='ROOK'
# board[7][7] ='ROOK'
# board[4][2] ='KNIGHT'
# pprint(board)

# from pprint import pprint
# empty='N'
# board=[[[empty for i in range(8)] for j in range(8)] for k in range(8)]
# pprint(board)

# Пока есть что делать делай это
# while conditional_expression:
#     instruction

# while True:
#     user_input=input('Enter a number, less than 10: ')
#     if int(user_input) < 10:
#         print('All is right')
#         print()
#         break
#     print()

# counter=0
# while counter<5:
#     print('Hello')
#     counter=counter+1

counter=5
while counter!=0:
    print('Hello')
    counter=counter-1

for i in range(5):
    print('hello')