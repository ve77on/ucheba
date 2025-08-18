#
# Создайте класс Car с атрибутами make, model и year. Добавьте метод display_info(),
# который выводит информацию о машине. Затем создайте объект этого класса и вызовите метод display_info().
# Требования:
# •	Программа должна создавать класс с названием Car, который содержит атрибуты make, model и year.
# •	Класс Car должен содержать метод display_info(), который выводит информацию о машине.
# •	Программа должна создавать объект класса Car.
# •	Программа должна вызывать метод display_info() для объекта класса Car.


class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Марка: {self.make}, model: {self.model}, year: {self.year}")


car1 = Car("Toyota", "Camry", 2015)

car1.display_info()


