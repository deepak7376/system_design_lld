

class Book(object):
    def __init__(self, book_id, title, authors, publishers, book_copies) -> None:
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publishers = publishers
        self.book_copy = book_copies

    def get_book_id(self):
        return self.book_id

    def get_title(self):
        return self.title


    