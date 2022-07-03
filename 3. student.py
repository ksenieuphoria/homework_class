'''
3. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age.
По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять
методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber.
Метод getName нужен для получения данных об имени конкретного студента,
метод getAge нужен для получения данных о возрасте конкретного студента,
метод setGroupNumber нужен для получения данных о номере группы конкретного студента.
Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию,
метод setGroupNumber позволяет изменить номер группы установленный по умолчанию.
В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.

'''

class Student:
    def __init__(self, name='Ivan', age = 18, groupNumber = '10A'):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber

    def getName(self):
        print(f"Name: {self.name}")

    def getAge(self):
        print(f"Age: {self.age}")

    def getGroupNumber(self):
        print(f"Group Number: {self.groupNumber}")

    def SetNameAge(self, a, b):
        self.name = a
        self.age = b

    def setGroupNumber(self, c):
        self.groupNumber = c
        print(f"Group Number: {self.groupNumber}")

Tony = Student("Tony", "20", "17B")
Cris = Student("Cris", "19", "17A")
Cassy = Student("Cassy", "18", "18B")
Effy = Student("Effy", "21", "14A")
Nina = Student("Nina", "17", "13B")
Tony.getName()
Tony.getAge()
Tony.getGroupNumber()

