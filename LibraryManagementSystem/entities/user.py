
class User(object):
    def __init__(self, user_id, name=None) -> None:
        self.user_id= user_id
        self.name = name
        self.borrowed_books = set()

    def get_user_id(self):
        return self.user_id

    def set_book(self, book_id):
        self.borrowed_books.add(book_id)

    def get_borrowed_books(self):
        return self.borrowed_books


