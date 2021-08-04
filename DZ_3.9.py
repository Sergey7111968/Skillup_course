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

    def get_car_information(self)-> str :
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

    def __setattr__(self, name, value): #Защищает от создания неправильных атрибутов
        if name in ['_Automobile__manufacture', '_Automobile__model', '_Automobile__price']:
            self.__dict__[name] = value

    def __getattr__(self, name): #Объясняет, что атрибут не существует
        if name not in ['_Automobile__manufacture', '_Automobile__model', '_Automobile__price']:
            return f'Атрибут "{name}" не существует!'

mycar = Automobile('Mazda', '6', 20000) #Создаем объект
mycar.get_car_information() #Получаем информацию (извлекаем все данные) про объект
mycar.__manufacture = 'VAZ' #Пробуем получить доступ к атрибуту 
print(mycar.__manufacture) #Пробуем вывести атрибут на печать 
mycar.set_car_information() #Меняем всю информацию про автомобиль 
# print(mycar.get_price())
