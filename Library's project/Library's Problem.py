from dataclasses import dataclass
from datetime import datetime, date
import copy


class Book:  # gradaranum grancvac grqeri bnutagir, qanak, sranov petq e nor grqer input anem, u durs grem
    def __init__(self, title, year, isbn, genre, ac, avc=0):
        self.title = title
        self.year = year
        self.international_standard_book_number = isbn
        self.genre = genre
        self.all_copies = ac
        self.available_copies = avc


class Student:  # usanoxi bnutagir, pordzelu em gradarani qart stexcel anhatakan numberov, yur.-in 10 grqic avel chtam,
    # nuyn grqic chtam, jamketnanc girq unenalu depqum urish girq chtam
    #s1-i poxaren karox enq grel s10001 (s(id)), nuyn kod@ qarti vra grvac klini, usanox@ heshtutyamb kgtnvi
    book_borrowing_limit = 10
    def __init__(self, name, age, id_number, email, faculty):
        self.name = name
        self.age = age
        self.id_number = id_number
        self.email = email
        self.faculty = faculty
        self.books_currently_taken = []
        self.books_taken = []

    def borrow_book(self, bookcopy):
        today = datetime.today()
        for student_book in self.books_taken:
            if (today - student_book.borrowed_date).days >= 14:
                return False

        bookcopy.borrowed_date = datetime.now()
        bookcopy.borrower = self
        bookcopy.status = 'on loan'

        self.books_taken.append(bookcopy)

    def current_status(self):
        for student_book in self.books_taken:
            print(f"{student_book.book.title}:")



    @property
    def bct(self):
        return self.books_currently_taken

    def displayInfo(self):  # class method
        print('Student Name: ', self.name,
              ', Age: ', self.age, ', ID: ', self.id_number,
              ', e-mail: ', self.email, ', Faculty: ', self.faculty,
              ', books currently taken: ', self.books_currently_taken,
              ', book borrowing limit: ', self.book_borrowing_limit)

class Library:
    def lib(self, student_list, book_list):
    # library_name = "YSU Library"
        self.student_list = student_list
        self.book_list = book_list

    def __str__(self):
        return f"{self.student_list}"

    def __repr__(self):
        return f"Library({self.student_list}, {self.book_list})"

    def add_book(self, new_book, book_list):
        book_list.append(new_book)

    def add_new_student(self, new_student, students_list):
        students_list.append(new_student)

    def find_book(self, book_list, title=None, isbn=None):
        find_book = []
        if title:
            for emt in book_list:
                if emt.name == title:
                    return find_book.append(emt)
        if isbn:
            for emt in book_list:
                if emt.id_number == isbn:
                    return find_book.append(emt)

    def find_all_books(self, title=None, isbn=None):
        found_book_list = []
        if title:
            for emt in found_book_list:
                if emt.name == title:
                    found_book_list.append(emt)
        elif isbn:
            for emt in found_book_list:
                if emt.isbn == isbn:
                    found_book_list.append(emt)
        else:
            raise ValueError("No arguments given!")

        return found_book_list

    print(find_book)

    print(find_all_books)

    def find_student(self, student_list,name=None, id_number=None):
        find_student_list = []
        if name:
            for element in student_list:
                if element.name == name:
                    return find_student_list.append(element)
        if id_number:
            for element in student_list:
                if element.id_number == id_number:
                    return find_student_list.append(element)

    def find_all(self, student_list, name=None, id_number=None):
        found_all_students = []
        if name:
            for element in student_list:
                if element.name == name:
                    found_all_students.append(element)
        elif id_number:
            for element in student_list:
                if element.id_number == id_number:
                    found_all_students.append(element)
        else:
            raise ValueError("No arguments given!")

        return found_all_students


    print(find_student)

    print(find_all)


    @property
    def students_count(self):
        return len(self.student_list)

    def remove_student(self, id_number):
        for idn in self.student_list:
            if idn.id_number == id_number:
                self.student_list.remove(idn)

    def account_by_number(self, id_number):
        for idn in self.student_list:
            if idn.account_number == id_number:
                return idn

@dataclass
class Bookcopy:
    book: Book
    borrower: Student
    borrowed_date: date


if __name__ == "__main__":
    id_number = input("Please enter the student's id: ")
    isbn = input("Please enter the book's ISBN: ")

    if id_number not in Student:
        raise Exception("Invalid logistics type")

    if isbn not in Book:
        raise Exception("Invalid logistics type")



s00001 = Student('Lilit Avetisyan', 22, 's00001', 'avetisyan.lilit.96@mail.ru', 'mechanica')
s00002 = Student('Lilith Avyan', 23, 's00002', 'avetisyan.96@mail.ru', 'mechanica')
s00003 = Student('Lilit Avetyan', 24, 's00003', 'avetisyan.lilit.@mail.ru', 'mechanica')
s00004 = Student('Lilith Avetisyan', 25, 's00004', 'avlilit.96@mail.ru', 'mechanica')

b10001 = Book("'Jane Eyre'Charlotte Brontë", 1847, 10001, "drama", 17)
##b1-i poxaren karox enq grel b10001 (b(isbn)), nuyn kod@ grqi vra grvac klini, girq@ heshtutyamb kgtnvi
b10002 = copy.deepcopy(b10001)
b10003 = copy.deepcopy(b10001)
b10004 = copy.deepcopy(b10001)
b20001 = Book('"Rich Dad Poor Dad" Robert Kiyosaki', 1997, 20001, "non-fiction", 22)
b20002 = copy.deepcopy(b20001)
