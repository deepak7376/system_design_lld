from entities.library import Library
from entities.rack import Rack
from entities.book import Book
from entities.user import User
from utils import add_list_elements_to_set, first_negative_index, count_total_negative_index, search_element_in_list


db = {}
book_copy_to_rack_no = {}
user = {}
def create_library(library_id, no_of_racks):
    # intialize library
    library = Library(library_id, no_of_racks)

    db[library_id] = library
    print(library.get_racks())
    print(f"Created library with {no_of_racks} racks")

#add_book <book_id> <title> <comma_separated_authors> 
#<comma_separated_publishers> 
#<comma_separated_book_copy_ids>
#add_book 1 book1 author1,author2 
#publisher1 book_copy1,book_copy2,book_copy3
def add_book(library_id:int, book_id:int, title:str, authors:set, publishers:set, book_copies:set)->None:

    # add book to rack
    library = db[library_id]
    rack = library.get_racks()

    # check if rack have any non-negative num.
    empty_rack = count_total_negative_index(rack)
    if empty_rack<len(book_copies):
        print("Rack not available")
        return
    # initialize book
    book = Book(book_id, title, authors, publishers, book_copies)

    temp = []
    for book_copy_id in list(book_copies):
        rack_no = first_negative_index(rack)
        temp.append(rack_no)
        rack[rack_no] = book_copy_id
    print(f"Added Book to racks: {temp}")
    print(rack)
    

def remove_book_copy(library_id, book_copy_id):

    library = db[library_id]
    rack = library.get_racks()

    idx = search_element_in_list(rack, book_copy_id)

    if idx == None:
        print("Invalid Book Copy ID")
        return

    #remove book
    rack[idx] = -1

    print(f"Removed book copy: {book_copy_id} from rack: {idx}")
    print(rack)

def borrow_book_copy(library_id, book_copy_id, user_id, due_date):
    # initialize the user
    user = user[user_id]
    library = db[library_id]
    rack = library.get_racks()

    if user.get_borrowed_books() > 5:
        print("Overlimit")
        return

    rack_no = search_element_in_list(rack, book_copy_id)
    if rack_no == None:
        print("Invalid Book ID")
        return

    #remove book
    rack[rack_no] = -1
    user.set_book(book_copy_id)
    
    print(f"Borrowed Book from rack: {rack_no}")

    
    






if __name__ == "__main__":
    create_library(1, 10)
    print(db)
    add_book(1, 1, "book1", ["author1","author2"], ["publisher1"] ,["book_copy1","book_copy2","book_copy3"])
    add_book(1, 2, "book2", [ "author2","author3"] ,["publisher2","publisher3"], ["book_copy4","book_copy5","book_copy6","book_copy7","book_copy8","book_copy9"])
    add_book(1, 3, "book3", ["author2"], ["publisher2"],[ "book_copy11","book_copy12","book_copy13"])
    # # print(book_copy_to_rack_no)
    remove_book_copy(1, "book_copy6")
    remove_book_copy(1, "book_copy13")