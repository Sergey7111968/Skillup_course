# print('Enter a, b :')
# a,b=map(int,input().split())
# while a<=b:
#     if a%7==0:
#         print(a)
#     a+=1

# counter=5
# while counter:
#     print('I am in :', counter)
#     counter-=1
# print('I am out')

# i=0
# while i<100:
#     print(i)
#     i=i+1

# for i in 'hello world':
#     print(i * 2, end='')

# for i in range(9,0,-1):
#     print(i)

# i=1
# while i<5:
#     print(i)
#     i+=1
#     if i==3:
#         break
# else:
#     print('Ended')

# while True:
#     i=input('Enter some text :')
#     if i =='End':
#         print('Goodbye')
#         break
#     if i:
#         print('Your entered :', i)
    
        
# print('Enter a, b :')
# a,b=map(int,input().split())
# for i in range(a,b):
#     if i%3==0:
#         print('Foo', i)
#     elif i%5==0:
#         print('Bar', i)
#     elif i%3==0 and i%5==0:
#         print('Foo Bar', i)
#     elif i%3!=0 and i%5!=0:
#         print(i)

# Tuple
# t= (1, 2, 'acd', True)
# print(type(t))

# dima=('Dima', 'Pupkin', 32)
# oleg=('Oleg', 'Ivanov', 30)
# people=[dima, oleg]
# print(people)

# a=("word", (2,'asdasd'), 1232)
# print(a[1][1])

# l=['word', True]
# t=(1, 2, 3, l)
# print(len(t))
# del l[1]
# print(t)

# tuple_1=(1, 2, 3, 4)
# tuple_2=(5, 6, 7, 8)
# tuple_3=tuple_1+tuple_2
# print(tuple_3)
# print(tuple_3*3)
# # for i in tuple_3:
# if 8 in tuple_3:
#     print(tuple_3.index(8))
# # print(i)

# A=('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat')
# day='Mons'
# if day in A:
#     num=A.index(day)
#     print('Number of day :', num+1)
# else:
#     # num=-1
#     print('Wrong day')

# tuple_1=(1, 2, 3, 4)
# tuple_2=(5, 6, 1, 2, 2, 2)
# tuple_3=tuple_1+tuple_2
# print(tuple_3.count(2))
# print(max(tuple_3))
# print(min(tuple_3))
# print(list(tuple_3))

# s={1, 2, 2, 2, 3, 4, 5}
# print(s)