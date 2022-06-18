from models.parking_lot import ParkingLot
from models.vehicle import Vehicle
from utils import get_parking_spot


class ParkingLotService(object):
    database = {}
    parking_pattern = None
    tickets = {}
    
    def __init__(self) -> None:
        self.parking_lot_id = None

    # create_parking_lot <parking_lot_id> <no_of_floors> <no_of_slots_per_floor>
    def create_parking_lot(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        parking_lot = ParkingLot(parking_lot_id, no_of_floors, no_of_slots_per_floor)
        self.__class__.parking_pattern = ["CAR" for _ in range(no_of_slots_per_floor)]
        self.__class__.parking_pattern[0] = "TRUCK"
        self.__class__.parking_pattern[1] = "BIKE"
        self.__class__.parking_pattern[2] = "BIKE"

        self.__class__.database[parking_lot_id] = parking_lot
        self.parking_lot_id = parking_lot_id
        print(f"Created parking lot with {no_of_floors} floors and {no_of_slots_per_floor} slots per floor")

    #park_vehicle <vehicle_type> <reg_no> <color>
    def park_vehicle(self, vehicle_type:str, reg_no:str, color:str):
        print(self.parking_lot_id)

        parking_lot = self.__class__.database[self.parking_lot_id]
        
        # initialize vehicle
        vehicle = Vehicle(vehicle_type, reg_no, color)

        # find spot for parking
        parking_lot_space = parking_lot.get_parking_space()
        floor_no, slot_no = get_parking_spot(parking_lot_space, vehicle_type, self.__class__.parking_pattern)
        
        if floor_no == -1 and slot_no == -1:
            print("Parking Lot Full")
            return
        # park vehicle
        parking_lot_space[floor_no][slot_no] = vehicle
        # create ticket
        ticket_id = f"{self.parking_lot_id}_{floor_no}_{slot_no}"
        # save ticket
        self.__class__.tickets[ticket_id] = (reg_no, color)
        print(f"Parked vehicle. Ticket ID: {ticket_id}")

    # unpark_vehicle <ticket_id>
    def unpark_vehicle(self, ticket_id):
        parking_lot_id, floor_no, slot_no = ticket_id.split("_")
        parking_lot = self.__class__.database.get(parking_lot_id)
        if parking_lot==None:
            print("Invalid Ticket")
            return
        parking_lot_space = parking_lot.get_parking_space()
        
        if self.__class__.tickets.get(ticket_id)==None or parking_lot_space[int(floor_no)][int(slot_no)]==-1:
            print("Invalid Ticket")
            return

        reg_no, color = self.__class__.tickets[ticket_id]
        #unpark vehicle
        parking_lot_space[int(floor_no)][int(slot_no)] = -1
        print(f"Unparked vehicle with Registration Number: {reg_no} and Color: {color}")

    # display_type: free_count, free_slots, occupied_slots
    def display(self, display_type, vehicle_type):
        parking_lot = self.__class__.database[self.parking_lot_id]
        parking_lot_space = parking_lot.get_parking_space()
        
        for floor_no in range(len(parking_lot_space)):
            no_of_free_slots = 0
            slot_nos = []
            occupied_slot_nos = []
            for slot_no in range(len(parking_lot_space[0])):
                slot_value = parking_lot_space[floor_no][slot_no]
                if slot_value==-1 and self.__class__.parking_pattern[slot_no]==vehicle_type:
                    no_of_free_slots+=1
                    slot_nos.append(slot_no)
                if slot_value!=-1 and self.__class__.parking_pattern[slot_no]==vehicle_type:
                    occupied_slot_nos.append(slot_no)
            
            if display_type == "free_count":
                print(f"No. of free slots for {vehicle_type} on Floor {floor_no}: {no_of_free_slots}")
            if display_type == "free_slots":
                print(f"Free slots for {vehicle_type} on Floor {floor_no}: {slot_nos}")
            if display_type == "occupied_slots":
                print(f"Occupied slots for {vehicle_type} on Floor {floor_no}: {occupied_slot_nos}")
        


    