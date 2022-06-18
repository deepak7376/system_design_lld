class Vehicle(object):
    def __init__(self, type, registration_number, color) -> None:
        self.type = type
        self.registration_number = registration_number
        self.color = color

    def get_type(self):
        return self.type

    def get_registration_number(self):
        return self.registration_number