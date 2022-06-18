class Rack(object):
    def __init__(self, rack_no) -> None:
        self.rack_no = rack_no
        self.book = None
        self.is_empty = True

    def get_rack_no(self):
        return self.rack_no

    def add_book(self, book):
        self.book = book
        self.is_empty = False

    def remove_book(self):
        self.book = None
        self.is_empty = True

    def get_book(self):
        return self.book