'''
2. Николай – оригинальный человек.
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет,
а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено,
даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к
экземпляру свойство «отчество» или метод «приветствие», то ничего у такого хитреца не получится).
Для ограничения количества наборов свойств и методов в экземпляре применяется специальный магический атрибут__slots__.

'''

class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        if self.name != "Николай":
            self.name = f'Я не {self.name}, а Николай'

        self.age = age

person1 = Nikola('Иван', 25)
person2 = Nikola('Николай', 21)
print(person1.name)
print(person2.name)