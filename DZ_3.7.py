# Домашнее задание

# Задание 1

# Реализуйте класс «Автомобиль». 
# Необходимо хранить в полях класса: название модели, год выпуска, производителя, 
# объем двигателя, цвет машины, цену. Реализуйте методы класса для ввода данных, 
# вывода данных, реализуйте доступ к отдельным полям через методы класса.

# class Car:

#     def __init__(self, model, year, manufacturer, engine, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine = engine
#         self.color = color
#         self.price = price

#     def update_car(self):
#         self.model = input('Введите модель: ')
#         self.year = input('Введите год: ')
#         self.manufacturer = input('Введите производителя: ')
#         self.engine = input('Введите объем двигателя: ')
#         self.color = input('Введите цвет: ')
#         self.price = input('Введите цену: ')

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         return self.year

#     def get_manufacturer(self):
#         return self.manufacturer

#     def get_engine(self):
#         return self.engine

#     def get_color(self):
#         return self.color

#     def get_price(self):
#         return self.price

# audi = Car('A6', 2018, 'Audi', 2.0, 'blue', 40000)
# audi.update_car()
# print(audi.get_model(), audi.get_year(), audi.get_manufacturer(), audi.get_engine(), audi.get_color(), audi.get_price())

# Задание 2

# Реализуйте класс «Книга». 
# Необходимо хранить в полях класса: название книги, год выпуска, издателя, жанр, автора, цену. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

class Book:

    def __init__(self, name, year, publisher, genre, autor, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.autor = autor
        self.price = price

    def update_book(self):
        self.name = input('Введите название книги: ')
        self.year = input('Введите год выпуска: ')
        self.publisher = input('Введите издателя: ')
        self.genre = input('Введите жанр: ')
        self.autor = input('Введите автора: ')
        self.price = input('Введите цену: ')

    def get_name(self):
        return self.name

    def get_year(self):
        return self.year

    def get_publisher(self):
        return self.publisher

    def get_genre(self):
        return self.genre

    def get_autor(self):
        return self.autor

    def get_price(self):
        return self.price

book1 = Book('Три товарища', 1935, 'Мир', 'Роман', 'Ремарк', 40)
book1.update_book()
print(book1.get_name(), book1.get_year(), book1.get_publisher(), book1.get_genre(), book1.get_autor(), book1.get_price())

# Задание 3

# Реализуйте класс «Стадион». 
# Необходимо хранить в полях класса: название стадиона, дату открытия, страну, город, вместимость. 
# Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.