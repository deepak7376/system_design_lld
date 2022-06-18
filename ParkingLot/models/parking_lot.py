class ParkingLot(object):
    def __init__(self, parking_lot_id, no_of_floors, no_of_slots_per_floor) -> None:
        self.parking_lot_id = parking_lot_id
        self.no_of_floors = no_of_floors
        self.no_of_slots_per_floor = no_of_slots_per_floor
        self.parking_lot = [[-1 for _ in range(no_of_slots_per_floor)] for _ in range(no_of_floors)]

    def get_lot_id(self):
        return self.parking_lot_id

    def assign_vehicle(self, floor_no, slot_no, vehicle):
        self.parking_lot[floor_no][slot_no] = vehicle

    def get_parking_space(self):
        return self.parking_lot