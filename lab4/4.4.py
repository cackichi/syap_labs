# Придумать класс самостоятельно, реализовать в нем методы экземпляра
# класса, статические, методы, методы класса
class Library:
    total_books = 0
    def __init__(self,name):
        self.name = name
        self.books = []
    def add_book(self, title, author):
        book = {"title":title, "author":author}
        self.books.append(book)
        Library.total_books += 1

    def remove_book(self,title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                Library.total_books -= 1

    def list_books(self):
        print("Все книги:")
        for book in self.books:
            print("Название: " + book["title"] + ", Автор: " + book["author"])

    @staticmethod
    def lib_info():
        print("Количество всех книг - " + Library.total_books.__str__())

    @classmethod
    def class_lib(cls, name):
        return cls(name)

lib = Library.class_lib("Библиотека")
lib.add_book("Война и мир","Толстой")
lib.add_book("Преступление и наказание", "Достоевский")
lib.list_books()
lib.lib_info()
lib.remove_book("Война и мир")
lib.list_books()
