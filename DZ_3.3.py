# Функция-декоратор, которая возводит в квадрат значение, которое возвращает функция, к которой применяется декоратор

def param_transfer(func):
   def wrapper(arg):
       print("Run function: " + str(func.__name__) +" with param: " + str(arg))
       print(func(arg**2))
   return wrapper

@param_transfer
def print_square(arg):
  return arg

# print_square = param_transfer(print_square)
print_square(6)

