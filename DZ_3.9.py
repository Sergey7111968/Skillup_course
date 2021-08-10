# Домашнее задание

# Разработайте класс с "полной инкапсуляцией", 
# доступ к атрибутам которого и изменение данных реализуются через вызовы методов. 
# В объектно-ориентированном программировании принято имена методов для извлечения данных 
# начинать со слова get (взять), а имена методов, в которых свойствам присваиваются значения, 
# – со слова set (установить). Например, get_Field, set_Field

class Automobile:
    def __init__(self, manufacture = str, model = str, price = int):
        self.__manufacture = manufacture
        self.__model = model
        self.__price = price

    def get_car_information(self) -> str:
        """Showing car information"""
        print(f'Автомобиль: {self.__manufacture} {self.__model} Цена: {self.__price}')

    def get_manufacture(self) -> str:
        """Return car information: manufacture"""
        return (self.__manufacture)

    def get_model(self) -> str:
        """Return car information: model"""
        return (self.__model)

    def get_price(self) -> int:
        """Return car information: price"""
        return (self.__price)

    def set_car_information(self):
        """Changes all car information"""
        self.__manufacture = input('Введите марку автомобиля: ')
        self.__model = input('Введите модель автомобиля: ')
        self.__price = int(input('Введите стоимость автомобиля: '))

    def __setattr__(self, name, value): #Защищает от создания атрибутов из основной ветки программы
        if name in ['_Automobile__manufacture', '_Automobile__model', '_Automobile__price']:
            self.__dict__[name] = value
        else:
            print('You can not do this')

    def __getattr__(self, name): #Объясняет, что атрибут не существует
        if name not in ['_Automobile__manufacture', '_Automobile__model', '_Automobile__price']:
            return f'Атрибут "{name}" не существует!'

mycar = Automobile('Mazda', '6', 20000) #Создаем объект
mycar.get_car_information() #Получаем информацию (извлекаем все данные) про объект
mycar.__manufacture = 'VAZ' #Пробуем получить доступ к атрибуту 
print(mycar.__manufacture) #Пробуем вывести атрибут на печать 
mycar.set_car_information() #Меняем всю информацию про автомобиль 
print(mycar.get_car_information())

# class Person:
#     def __init__(self, surname: str, name: str, id: str):
#         self.__surname = surname
#         self.__name = name
#         self.__id = id

#     def get_data(self):
#         """Get full data"""
#         return f'Person data: \n'\
#                 f'\t Surname: {self.__surname}\n'\
#                 f'\t Name: {self.__name}\n'\
#                 f'\t ID: {self.__id}'

#     def get_surname(self):
#         """Get surname"""
#         return self.__surname

#     def get_name(self):
#         """Get name"""
#         return self.__name

#     def get_id(self):
#         """Get ID"""
#         return self.__id

#     @staticmethod
#     def __check_sur_name(value):
#         """Name and surname check"""
#         if isinstance(value, str) and value.isalpha:
#             return True

#     def set_surname(self, value):
#         """Setting new surname"""
#         if Person.__check_sur_name(value):
#             self.__surname = value.capitalize()
#         else:
#             print(f'"{value}" cannot be surname')

#     def set_name(self, value):
#         """Setting new name"""
#         if Person.__check_sur_name(value):
#             self.__name = value.capitalize()
#         else:
#             print(f'"{value}" cannot be name')

#     def set_id(self, value):
#         """Setting new ID"""
#         if isinstance(value, str) and len(value) == 10 and value.isdigit():
#             self.__id = value
#         else:
#             print(f'"{value}" cannot be id')

#     def __setattr__(self, attr, value):
#         if attr in ['_Person__surname', '_Person__name', '_Person__id']:
#             self.__dict__[attr] = value
#         else:
#             print(f' {attr} cannot be personal data')

#     def __getattr__(self, attr):
#         if attr not in self.__dict__:
#             return f' {attr} - such data an unavailable '

#     #Results

# if __name__ == '__main__':
#     a = Person('Ivanov', 'Ivan', '1234567890')

# #попытка получить доступ к данным вне класса
# print(a.__surname)
# print(a.__name)
# print(a.__id)

# #извлечение данных с помощью методов класса
# print(a.get_data()) #Все данные

# print(a.get_surname())
# print(a.get_name())
# print(a.get_id())

# #Присваивание новых значений и доступ у ним, если они соответствуют условиям
# a.set_surname('johnson')
# print(a.get_surname())

# a.set_name('jpnh')
# print(a.get_name())

# a.set_id('0987654320')
# print(a.get_id())

# #Попытка создать новый атрибут и извлечь атрибут которого нет
# a.password = "jhfrse5676"
# print(a.password)

                
