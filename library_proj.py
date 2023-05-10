
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from pprint import pprint


@dataclass()
class Book:
    title: str
    authors: str
    year: int
    isbn: int
    ganre: str
    all_copies: list = field(default_factory=list)
    available_copies: list = field(default_factory=list)

    def __repr__(self):
        return f"{self.title} by {self.authors}"


    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn


    def add_new_copy(self, copy):
        self.all_copies.append(copy)
        if copy.availability_status == "available":
            self.available_copies.append(copy)


    def get_available_copies(self):
        return f"Available copies: {self.available_copies}"


    def remove_copy(self, copy):
        if copy in self.available_copies:
            self.available_copies.remove(copy)


@dataclass()
class BookCopy:
    book: Book
    copy_id: int
    borrower: str = None
    borrowed_date: datetime = None
    availability_status: str = "available"
    condition_rating: int = None

    # def __repr__(self):
    #     return f"{self.book}"

    def borrow_this_copy(self, student):
        if self.availability_status == "available":
            self.borrower = student
            self.borrowed_date = datetime.now()
            self.availability_status = "on loan"
            self.book.available_copies.remove(self)
            student.taken_books.append(self)
        else:
            print("This book copy is not available for borrowing.")

    def return_this_copy(self):
        if self.availability_status == "on loan":
            self.borrower = None
            self.borrowed_date = None
            self.availability_status = "available"
            self.book.available_copies.append(self)

    def change_condition_rating(self, condition_rating):
        if not isinstance(condition_rating, int) or condition_rating < 1 or condition_rating > 10:
            raise ValueError("Condition rating must be between one and ten")
        else:
            self.condition_rating = condition_rating


class Student:
    def __init__(self, name, id, email, borrowing_limit=5):
        self.name = name
        self.id = id
        self.__email = email
        self.taken_books = []
        self.borrowing_limit = borrowing_limit

    def __repr__(self):
        return f"{self.name}, ID: {self.id}"

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    def __str__(self):
        return f"{self.name}, ID: {self.id}"

    def borrow_book(self, book_copy: BookCopy):

        if book_copy in self.taken_books:
            print("You cannot borrow the same book copy twice.")
        elif len(self.taken_books) >= self.borrowing_limit:
            print("You have reached your borrowing limit.")
        elif book_copy.availability_status == "on loan":
            print("This book copy is not available for borrowing.")
        else:
            due_date = datetime.now() + timedelta(days=14)
            book_copy.borrow_this_copy(self)
            print(f"You have successfully borrowed {book_copy.book.title}. It is due on {due_date}.")

    def return_book(self, book_copy: BookCopy):
        if book_copy in self.taken_books:
            self.taken_books.remove(book_copy)
            print(f"You have successfully returned {book_copy.book.title}.")
        else:
            print("You did not borrow this book copy.")

    @property
    def current_status(self):
        print(f"{self.name}'s borrowed books:")
        status = []

        for book_copy in self.taken_books:
            due_date = book_copy.borrowed_date + timedelta(days=14)
            status.append((book_copy.book.title, book_copy.copy_id, due_date))
        return status


class Library:
    def __init__(self):
        self.owned_books = []
        self.registrates_students = []

    def add_new_book(self, book):
        for books in book.all_copies:
            if books in self.owned_books:
                raise Exception("Book is already in Library")
            else:
                self.owned_books.append(book)

    def remove_book(self, book):
        self.owned_books.remove(book)

    def add_student(self, *students):
        for student in students:
            if student in self.registrates_students:
                raise Exception("Student is already registered!")
            else:
                self.registrates_students.append(student)

    def remove_student(self, student):
        if student in self.registrates_students:
            self.registrates_students.remove(student)

    @staticmethod
    def change_borrowing_limit(student):
        for book in student.taken_books:
            limit = student.borrowing_limit - 1
        return f"{student} can borrow {limit} books"

    def see_all_books(self):
        return self.owned_books

    def see_oll_available_books(self):
        available_books = []
        for book in self.owned_books:
            available_copies = book.get_available_copies()
            if len(available_copies) > 0:
                available_books.append((book, available_copies))
        return available_books

    def search_book_by_author(self, authores):
        result = []
        for book in self.owned_books:
            if book.author == authores:
                result.append(book)
        return result

    def search_book_by_title(self, title):
        result = []
        for book in self.owned_books:
            if book.title == title:
                result.append(book)
        return result


book1 = Book("The Picture Of Dorian Gray", "Oskar Wald", 1890, 123456, "Fantasy")
book2 = Book("Anna Karenina", "Lev Tolstoy", 1912, 114455, "Novel")
book3 = Book("Hamlet", "Shekspir", 1962, 4455889, "Novel")
book4 = Book("Fahrenheit 451", "Ray Bradbury", 1953, 125874, "Fantasy")

student1 = Student("Mheryan Davit", 111, "mheryan@gmail.com")
student2 = Student("Santuryan Tatevik", 222, "tateviksanturyan@gmail.com")
book_copy1 = BookCopy(book1, 123)
book_copy1_1 = BookCopy(book1, 124)
book_copy1_2 = BookCopy(book1, 125)
book_copy2_1 = BookCopy(book2, 117)
book_copy2_2 = BookCopy(book2, 118)
book_copy2_3 = BookCopy(book2, 119)
book_copy2_4 = BookCopy(book2, 116)
book_copy3 = BookCopy(book3, 777)
book_copy3_1 = BookCopy(book3, 778)
book_copy4 = BookCopy(book4, 254)
book_copy4_1 = BookCopy(book4, 255)
book_copy4_2 = BookCopy(book4, 256)
book_copy1.book.add_new_copy(book_copy1)
book_copy1_1.book.add_new_copy(book_copy1_1)
book_copy1_2.book.add_new_copy(book_copy1_2)
book_copy2_2.book.add_new_copy(book_copy2_2)
book_copy2_3.book.add_new_copy(book_copy2_3)
book_copy2_4.book.add_new_copy(book_copy2_4)
book_copy3.book.add_new_copy(book_copy3)
book_copy3_1.book.add_new_copy(book_copy3_1)
book_copy4.book.add_new_copy(book_copy4)
book_copy4_1.book.add_new_copy(book_copy4_1)
book_copy4_2.book.add_new_copy(book_copy4_2)
book_copy1.borrow_this_copy(student1)
book_copy1_1.borrow_this_copy(student1)
student1.borrow_book(book_copy1_2)
pprint(book_copy2_1.book.available_copies)
pprint(student1.taken_books)
pprint(book_copy1_1.availability_status)
# books = [book1, book2, book3, book4]
students = [student1, student2]
library = Library()
library.add_new_book(book1)
library.add_new_book(book2)
library.add_new_book(book3)
library.add_new_book(book4)
library.add_student(students)

pprint(library.registrates_students)
pprint(library.owned_books)
pprint(library.search_book_by_title("Hamlet"))
pprint(library.change_borrowing_limit(student1))
pprint(book1.get_available_copies())