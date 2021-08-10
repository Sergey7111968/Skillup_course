# class B:
#     count = 0
#     def __init__(self):
#         B.count += 1
#     def __del__ (self):
#         B.count -= 1

# a = B()
# b = B()

# print(B.count)
# del a
# print(B.count)
# B.count -= 1
# print(B.count)

# class B:
#     __count = 0
#     def __init__(self):
#         B.__count += 1
#     def __del__ (self):
#         B.__count -= 1
#     @ staticmethod
#     def qty_object():
#         return B.__count

# a = B()
# print(a.qty_object())

# print(B.__count)
# B.__count -= 1 
# B._B__count += 1 Never do like this
# print(B._B__count)

# class Doublelist:
#     def __init__(self, l: list):
#         self.double = Doublelist.__make_double(l)
#     def __make_double(old_list: list) -> list:
#         new_list = []
#         for i in old_list:
#             new_list.append(i)
#             new_list.append(i)
#         return new_list

# nums = Doublelist(l = [1,2,3,6,12])
# print(nums.double)
# print(Doublelist.__make_double([1,2]))

# class A:
#     def __init__(self, value):
#         self.field1 = value
    
# a = A(value=10)
# a.field2 = 20
# print(a.field1, a.field2)

# class A(object):
#     def __init__(self):
#         pass
#     def foo(self):
#         print('I am in A')

# class B(A):
#     def foo(self):
#         super().foo()

# b=B()
# b.foo()


# class A:
#     def __init__(self, value):
#         self.field1 = value
#     def __setattr__(self, attr, value):
#         # super().__setattr__(attr, value)
#         if attr in ['field1']:
#             self.__dict__[attr] = value
#         else:
#             raise AttributeError('You can not do this')
        
#     # def __getattr__(self, name):
#     #     if name not in self.__dict__:
#     #         raise AttributeError(f"{self} has no attribute '{name}'")
        
    
# a = A(value='Text')
# # a.counter = 20
# print(a.field1)
# print(getattr(a, 'field2', 'Hello'))
# print(a.__dict__)

# ingradients = {
#     'potato': 3,
#     'tomato': 2,
#     'apple': 12
# }

# class Dish:
#     def __init__(self, ingradients: dict):
#         for key, value in ingradients.items():
#             setattr(self, key, value)
#     def __getattr__(self, name):
#         return f'This dish has no {name}'

# dish = Dish(ingradients=ingradients)
# # print(dish.potato)
# # print(dish.fish)

# soup_ingradients = {
#     'water': 1,
#     'potato': 3,
#     'meat': 0.5
# }

# soup = Dish(ingradients=soup_ingradients)

# def check_dish(dish: Dish, ingradients: dict) -> str:
#     for key, value in ingradients.items():
#         attr = getattr(dish, key, False)
#         if not attr or attr != value:
#             return 'This is not a soup'
#     return 'This is a soup'

# print(check_dish(dish=dish, ingradients=soup_ingradients))
# print(check_dish(dish=soup, ingradients=soup_ingradients))

