'''
1. Создайте класс Soda (для определения типа газированной воды),
принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
В этом классе реализуйте метод show_my_drink(),
выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
а иначе отобразится следующая фраза: «Обычная газировка».

'''

class Soda:
    def __init__(self, addition):
        if isinstance(addition, str):
            self.addition = addition
        else:
            self.addition = None


    def show_my_drink(self):
        if self.addition:
            print(f'Газировка и {self.addition}')
        else:
            print('Обычная газировка')


drink1 = Soda(0)
drink2 = Soda('сироп')
drink3 = Soda(5)
drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()