'''
Напишите программу с классом Math. Создайте два атрибута — a и b.
Напишите методы addition — сложение, multiplication — умножение,
division — деление, subtraction — вычитание.
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.
'''

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        try:
            if self.b != 0:
                return self.a / self.b
        except ZeroDivisionError:
            print('деление на 0')

    def subtraction(self):
        return self.a - self.b

total = Math(5, 3)
print(total.multiplication())
print(total.addition())
print(total.division())
print(total.subtraction())


