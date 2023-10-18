# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод
# выводит сообщение «Запуск отрисовки»; создать три дочерних класса Pen
# (ручка), Pencil (карандаш), Handle (маркер); в каждом классе реализовать
# переопределение метода draw. Для каждого класса метод должен выводить
# уникальное сообщение; создать экземпляры классов и проверить, что
# выведет описанный метод для каждого экземпляра.
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки - " + self.title)

class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки Pen - " + self.title)
class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки Pencil - " + self.title)
class Heandle(Stationery):
    def draw(self):
        print("Запуск отрисовки Heandle - " + self.title)

stat = Stationery("stationery")
pen = Pen("pen")
pencil = Pencil("pencil")
heandle = Heandle("heandle")

stat.draw()
pen.draw()
pencil.draw()
heandle.draw()