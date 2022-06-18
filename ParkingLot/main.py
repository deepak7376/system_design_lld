from service.parking_lot_service import ParkingLotService


def main():
    parking_lot_service = ParkingLotService()
    while True:      
        try:
            user_input = input().split(" ")
            if user_input[0] == "create_parking_lot":
                parking_lot_service.create_parking_lot(user_input[1], int(user_input[2]), int(user_input[3]))
            elif user_input[0] == "park_vehicle":
                #park_vehicle <vehicle_type> <reg_no> <color>
                parking_lot_service.park_vehicle(user_input[1], user_input[2], user_input[3])
            elif user_input[0] == "unpark_vehicle":
                # unpark_vehicle <ticket_id>
                parking_lot_service.unpark_vehicle(user_input[1])
            elif user_input[0] == "display":
                parking_lot_service.display(user_input[1], user_input[2])
            elif user_input[0]=="exit":
                break
            else:
                print("Invalid")        
        except ValueError:
            continue

if __name__ == "__main__":
    main()