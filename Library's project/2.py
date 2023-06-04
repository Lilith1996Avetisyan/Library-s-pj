class Library:
    def __init__(self, name):
        self.name = name
        self.books_available = []
        self.books_taken = []

    def add_book(self, book):
        self.books_available.append(book)

    def remove_book(self, book):
        if book in self.books_available:
            self.books_available.remove(book)
        else:
            print(f"The book '{book}' is not available in the library.")

    def take_book(self, book):
        if book in self.books_available:
            self.books_available.remove(book)
            self.books_taken.append(book)
        else:
            print(f"The book '{book}' is not available in the library.")

    def return_book(self, book):
        if book in self.books_taken:
            self.books_taken.remove(book)
            self.books_available.append(book)
        else:
            print(f"The book '{book}' is not taken by any student.")

    def find_book(self, title):
        for book in self.books_available:
            if book.title.lower() == title.lower():
                return book
        return None

    def print_available_books(self):
        print(f"Available books in the library '{self.name}':")
        for book in self.books_available:
            print(book.title)

    def print_taken_books(self):
        print(f"Books currently taken from the library '{self.name}':")
        for book in self.books_taken:
            print(book.title)


class Book:
    def __init__(self, title, author, year, isbn, ac):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.all_copies = ac
        self.year = year


class BookCopy:
    def __init__(self, book):
        self.book = book

    def __str__(self):
        return f"Copy of '{self.book.title}' by {self.book.author}"

class Student:
    def __init__(self, name, age, id_number, email, faculty):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.email = email
        self.faculty = faculty
        self.books_currently_taken = []

    def take_book_from_library(self, library, book_title):
        book = library.find_book(book_title)
        if book is not None:
            library.take_book(book)
            book_copy = BookCopy(book)
            self.books_currently_taken.append(book_copy)
        else:
            print(f"The book '{book_title}' is not available in the library.")

    def return_book_to_library(self, library, book_title):
        for book_copy in self.books_currently_taken:
            if book_copy.book.title.lower() == book_title.lower():
                library.return_book(book_copy.book)
                self.books_currently_taken.remove(book_copy)
                return
        print(f"You haven't taken the book '{book_title}'.")


if __name__ == "__main__":
    student_list = [
        Student('Lilit Avetisyan', 22, 's00001', 'avetisyan.lilit.96@mail.ru', 'mechanica'),
        Student('Lilith Avyan', 23, 's00002', 'avetisyan.96@mail.ru', 'mechanica'),
        Student('Lilit Avetyan', 24, 's00003', 'avetisyan.lilit.@mail.ru', 'mechanica'),
        Student('Lilith Avetisyan', 25, 's00004', 'avlilit.96@mail.ru', 'mechanica')
    ]

    book_list = [
        Book('Jane Eyre', "Charlotte Brontë", 1847, 10001, 17),
        Book("Rich Dad Poor Dad", 'Robert Kiyosaki', 1997, 20001, 22),
        Book("The Pragmatic Programmer", "Andrew Hunt, David Thomas", 1999, 30001, 11)
    ]

    library = Library("Library YSU")
    for book in book_list:
        library.add_book(book)

    library.print_available_books()

    student_list[0].take_book_from_library(library, "Lilit Avetisyan")
    student_list[1].take_book_from_library(library, "s00002")
    student_list[2].take_book_from_library(library, "mechanica")

    library.print_taken_books()

    student_list[1].return_book_to_library(library, "Python Course")

    library.print_taken_books()

    student_list[1].return_book_to_library(library, "Python Crash Course")

    library.print_taken_books()
