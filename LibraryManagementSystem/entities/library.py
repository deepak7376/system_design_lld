class Library(object):
    def __init__(self, library_id, no_of_racks) -> None:
        self.library_id = library_id
        self.racks = [-1 for _ in range(no_of_racks)]

    def get_racks(self):
        return self.racks






    