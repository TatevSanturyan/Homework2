from datetime import datetime, timedelta


class Book:
    def __init__(self, title: str, authors: str, year: int, isbn: int, ganre: str):
        self.title = title
        self.authors = authors
        self.year = year
        self.isbn = isbn
        self.ganre = ganre
        self.all_copies = []
        self.available_copies = []

    def __str__(self):
        return f"{self.title} by {self.authors}"

    def __eq__(self, other):
        return isinstance(other, Book) and self.isbn == other.isbn

    def add_new_copy(self,copy):
        self.all_copies.append(copy)
        self.available_copies.append(copy)

    @property
    def availablecopies(self):
        return self.available_copies




class BookCopy:
    def __init__(self, copy_id: int, borrower: str = None, borrowed_date: datetime = None,
                 condition_rating: int = None):
        self.book = Book("The Picture Of Dorian Gray", "Oskar Wald", 1890, 123456, "Fantasy")
        self.copy_id = copy_id
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.availability_status = "available"
        self.condition_rating = condition_rating

    def __str__(self):
        return f"{self.book}"

    def borrow_this_copy(self, student):
        if self.availability_status == "available":
            self.borrower = student
            self.borrowed_date = datetime.now()
            self.availability_status = "on loan"
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

book_copy1 = BookCopy( 123)
book_copy1.book.add_new_copy(book_copy1)
print(book_copy1.book.available_copies)
# book_copy1.borrow_this_copy("Mheryan Davit")


class Student:
    def __init__(self, name, id, email, borrowing_limit=5):
        self.name = name
        self.id = id
        self.email = email
        self.taken_books = []
        self.borrowing_limit = borrowing_limit

    def __str__(self):
        return f"{self.name}, ID: {id}"

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

    def current_status(self):
        print(f"{self.name}'s borrowed books:")

        for book_copy in self.taken_books:
            due_date = book_copy.borrowed_date
            due_date += timedelta(days=14)


student1 = Student("Mheryan Davit", 111, "mheryan@gmail.com")
print(student1.__dict__)


class Library:
    def __init__(self):
        self.owned_books = []
        self.registrates_students = []

    def add_new_book(self, book):
        self.owned_books.append(book)

    def remove_book(self, book):
        self.owned_books.remove(book)

    def add_student(self, student):
        if student in self.registrates_students:
            raise Exception("Student is already registered!")
        else:
            self.registrates_students.append(student)

    def remove_student(self, student):
        if student in self.registrates_students:
            self.registrates_students.remove(student)

    def change_borrowing_limit(self, student, new_limit):
        student.borrowing_limit = new_limit

    def see_all_books(self):
        return self.owned_books

    def see_oll_available_books(self):
        available_books = []
        for book in self.owned_books:
            available_copies = book.get_available_copies()
            if len(available_copies) > 0:
                available_books.append((book, available_copies))
        return available_books

    def search_book_by_author(self, author):
        result = []
        for book in self.owned_books:
            if book.author == author:
                result.append(book)
        return result

    def search_book_by_title(self, title):
        result = []
        for book in self.owned_books:
            if book.title == title:
                result.append(book)
        return result
