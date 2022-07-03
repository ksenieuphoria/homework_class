'''
5.Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса
Car — color (цвет), type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля,
при его вызове выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит
 сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение
 автомобилю типа. Пятый — присвоение автомобилю цвета.

'''

class Car():

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def go(self):
        return f'Автомобиль заведен'

    def stop(self):
        return f'Автомобиль заглушен'

    def car_year(self, a):
        self.year = a
        return f'Год выпуска: {self.year}'

    def car_type(self, b):
        self.type = b
        return f'Марка: {self.type}'

    def car_color(self, c):
        self.color = c
        return f'Цвет: {self.color}'

car = Car('red', 'lamborghini', 2022)
print(car.go())
print(car.stop())
print(car.car_type('huracan'))
print(car.car_year(2022))