# Создать класс List (список), в котором реализовать методы для работы со
# списком (не менее 5).
class List:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)

    def get_len(self):
        return len(self.items)

    def get_item(self, index):
        if 0 <= index < self.get_len():
            return self.items[index]
        else:
            return None

    def clear(self):
        self.items = []
