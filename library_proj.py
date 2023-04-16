from datetime import datetime
class Book:
    def __init__(self,title, authors, year, isbn, ganre):
        self.title = title
        self.authors = authors
        self.year = year
        self.isbn = isbn
        self.ganre = ganre
        self.all_copies = []
        self.available_copies = []

    def __str__(self):
        return f"{self.title} by {self.authors}"

    def add_new_copy(self, copy):
        self.all_copies.append(copy)
        self.available_copies.append(copy)

    @property
    def availablecopies(self):
        return self.available_copies

class BookCopy:
    def __init__(self, book, copy_id, borrower = None, borrowed_date = None, condition_rating = None):
        self.book = book
        self.copy_id = copy_id
        self.borrower = borrower
        self.borrowed_date = borrowed_date
        self.availability_status = "available"
        self.condition_rating = condition_rating

    def borrow_this_copy(self, student):
        if self.availability_status =="available":
            self.borrower = student
            self.borrowed_date = datetime.now()
            self.availability_status = "is taken"
            pass


    def return_this_copy(self, copy):
        pass

    def change_condition_rating(self):
        pass



class Student:
    def __init__(self, name, id, email, book_borrowing_limit = 5):
        self.name = name
        self.id = id
        self.email = email
        self.taken_books = []
        self.book_borrowing_limit = book_borrowing_limit

    def __str__(self):
        return f"{self.name}, ID: {id}"

    def borrow_book(self, book):
        pass

    def return_book(self, book):
        pass

    def current_status(self):
        print(f"You borraw:{self.taken_books} books at ")



class Library:
    def __init__(self):
        self.owned_books = []
        self.registrates_students = []

    def add_new_book(self, book):
        self.owned_books.append(book)

    def remove_book(self,book):
        self.owned_books.remove(book)

    def add_student(self, student):
        if student  in self.registrates_students:
            raise Exception("Student is already registred!")
        else:
            self.registrates_students.append(student)


    def remove_student(self,student):
        if student in self.registrates_students:
            self.registrates_students.remove(student)

    def change_borrowing_limit(self,new_limit):
        pass

    def see_all_books(self):
        return self.owned_books

    def see_oll_available_books(self):
        pass

    def search_book_by_author(self, author):
        # if Book.authors == author
        pass
    def search_book_by_title(self, title):
        pass
