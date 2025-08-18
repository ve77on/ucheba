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


# class Library:
#     def __init__(self, books):
#         self.books = books
#
#     def add_book(self, name_book):
#         self.books.append(name_book)
#
#     def display_books(self):
#         print(f"Books: {self.books}")
#
#
# collection = Library([])
#
# collection.add_book("Harry Potter")
# collection.display_books()


# Создайте класс Rectangle с конструктором, который принимает параметры width и height.
# Добавьте метод area(), который возвращает площадь прямоугольника. Создайте объект этого класса и вычислите его площадь.
# Требования:
# •	Программа должна включать класс Rectangle, который содержит конструктор с параметрами width и height.
# # •	В классе Rectangle должен быть метод area(), который возвращает площадь прямоугольника, рассчитанную как произведение ширины и высоты.
# # •	Необходимо создать объект класса Rectangle с заданными шириной и высотой.
# # •	С помощью метода area() создаденного объекта необходимо вычислить и вывести площадь прямоугольника.
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         print(self.width * self.height)
#
#
# rectangle1 = Rectangle(5, 10)
#
# rectangle1.area()
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#
# rectangle1 = Rectangle(5, 10)
#
# print(rectangle1.area())
#
# Банкир.
# Создайте класс BankAccount с конструктором, который принимает параметры account_number и initial_balance.
# Добавьте метод deposit(amount), который пополняет счет, и метод withdraw(amount), который снимает средства со счета.
# Создайте объект этого класса и выполните несколько операций пополнения и снятия средств.
# Требования:
# •	Программа должна включать класс BankAccount, который имеет конструктор, принимающий параметры account_number и initial_balance.
# •	Класс BankAccount должен содержать метод deposit(amount), который увеличивает баланс счета на указанную сумму.
# •	Класс BankAccount должен иметь метод withdraw(amount), который уменьшает баланс счета на указанную сумму при условии наличия достаточных средств.
# •	Программа должна создать объект класса BankAccount и выполнить несколько операций по пополнению и снятию средств, демонстрируя работу методов deposit и withdraw.


# class BankAccount:
#     def __init__(self, account_number, initial_balance):
#         self.account_number = account_number
#         self.initial_balance = initial_balance
#
#     def deposit(self, amount):
#         self.initial_balance = self.initial_balance + amount
#         print(f"Остаток на счету {self.initial_balance}")
#
#     def withdraw(self, amount):
#         if self.initial_balance < amount:
#             print(f"Недостаточно средств, Остаток на счету {self.initial_balance}")
#         else:
#             self.initial_balance = self.initial_balance - amount
#             print(f"Остаток на счету {self.initial_balance}")
#
# account1 = BankAccount(123, 1500)
# account1.deposit(50)
# account1.withdraw(500)

# Создайте класс Car, который будет иметь публичный атрибут brand и защищенный атрибут _model_.
# Добавьте методы для получения и установки значения защищенного атрибута _model_.
# Создайте объект класса Car, установите значения атрибутов и выведите их на экран.
# Требования:
# •	Программа должна включать создание класса Car.
# •	Класс Car должен содержать публичный атрибут brand, который можно будет свободно изменять и читать.
# •	Класс Car должен содержать защищенный атрибут _model_, доступ к которому должен осуществляться через методы получения и установки значения.
# •	Класс Car должен содержать метод для получения значения защищенного атрибута _model_ и метод для установки значения защищенного атрибута _model_.
# •	Программа должна создать объект класса Car, установить значения атрибутов brand и _model_, используя публичные и защищенные методы доступа, и вывести эти значения на экран.
#
# class Car:
#     def __init__(self, brand, _model):
#         self.brand = brand
#         self._model = _model
#
#     def get_model(self):
#         return self._model
#
#     def set_model(self,_model):
#         self._model = _model
#
# car1 = Car("Toyota", "Rav4")
# car1.set_model("Prius")
# print(car1.get_model())
# print(car1.brand)

# Библиотека.
# Создайте класс Library, который будет представлять библиотеку книг.
# Добавьте метод __str__, который будет возвращать строку с информацией о библиотеке с перечнем книг,
# и метод __len__, который будет возвращать количество книг в библиотеке. Создайте объект класса Library,
# добавьте в него несколько книг и выведите информацию о библиотеке и количество книг.
# Требования:
# •	Программа должна включать класс Library, который представляет библиотеку книг.
# •	В классе Library должен быть метод __str__, который возвращает строковую информацию о библиотеке с перечнем книг.
# •	В классе Library должен быть метод __len__, который возвращает количество книг в библиотеке.
# •	Должна быть возможность добавлять книги в объект класса Library.
# •	Программа должна выводить информацию о библиотеке с перечнем книг и количество книг с использованием методов __str__ и __len__.

class Library:
    def __init__(self, *books):
        self.books = list(books)

    def lib_append(self, book_name):
        self.books.append(book_name)

    def __str__(self):
        return f"Books: {self.books}"

    def __len__(self):
        return len(self.books)
lib1 = Library("1994")
lib1.lib_append("HP")
print(lib1.__str__())
print(lib1.__len__())


















