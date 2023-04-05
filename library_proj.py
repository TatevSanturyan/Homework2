class Book:
    def __init__(self, title, authors, year, ISBN, genre):
        self.title = title
        self.authors = authors
        self.year = year
        self.ISBN = ISBN
        self.genre = genre
        self.all_copies = []
        self.availabal_copies = []

    def add_copy(self, copy):
        self.all_copies.append(copy)
        pass
    def get_available_copies(self, copy):
        pass


class BookCopy:
    def __init__(self, book, copy_id):
        self.book = book
        self.copy_id = copy_id
        self.the_borrower = None
        self.borrowed_date = None
        self.availability_status = "available"
        self.condition_reyting = range(1, 11)

    def borrow_this_copy(self):
        pass

    def return_this_copy(self):
        pass

    def change_condition_rating(self):
        pass


class Student:
    def __init__(self, name, ID, email, book_borrowing_limit=5):
        self.name = name
        self.ID = ID
        self.email = email
        self.books_currently_taken = []
        self.book_borrowing_limit = book_borrowing_limit

    def borrow_book(self):
        pass

    def return_book(self):
        pass

    def get_status(self):
        pass


class Library:
    def __init__(self):
        self.owned_books = []
        self.students = []

    def add_books(self):
        pass

    def remove_books(self):
        pass

    def add_students(self):
        pass

    def remove_students(self):
        pass

    def change_borrowing_limit(self):
        pass

    def det_all_books(self):
        pass

    def get_available_books(self):
        pass

    def search_book_by_title(self, title):
        pass

    def search_book_by_author(self, author):
        pass
