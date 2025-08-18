# #
# # Создайте класс Car с атрибутами make, model и year. Добавьте метод display_info(),
# # который выводит информацию о машине. Затем создайте объект этого класса и вызовите метод display_info().
# # Требования:
# # •	Программа должна создавать класс с названием Car, который содержит атрибуты make, model и year.
# # •	Класс Car должен содержать метод display_info(), который выводит информацию о машине.
# # •	Программа должна создавать объект класса Car.
# # •	Программа должна вызывать метод display_info() для объекта класса Car.
#
#
# class Car:
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model = model
#         self.year = year
#
#     def display_info(self):
#         print(f"Марка: {self.make}, model: {self.model}, year: {self.year}")
#
#
# car1 = Car("Toyota", "Camry", 2015)
#
# car1.display_info()


# Создайте класс Library с атрибутом books, который представляет собой список книг.
# Добавьте методы add_book(book) для добавления книги в библиотеку и display_books() для вывода списка всех книг.
# Создайте объект класса Library, добавьте несколько книг и выведите список книг, используя методы объекта.
# Требования:
# •	Программа должна включать класс Library с атрибутом books, представляющим собой список книг.
# •	Класс Library должен содержать метод add_book(book), который добавляет книгу в список books.
# •	Класс Library должен содержать метод display_books(), который выводит список всех книг.
# •	Программа должна создавать объект класса Library.
# •	Программа должна использовать методы add_book(book) и display_books() на созданном объекте для добавления книг и вывода списка книг.


class Library:
    def __init__(self, books):
        self.books = books

    def add_book(self, name_book):
        self.books.append(name_book)

    def display_books(self):
        print(f"Books: {self.books}")


collection = Library([])

collection.add_book("Harry Potter")
collection.display_books()









