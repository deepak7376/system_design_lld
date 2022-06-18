def get_parking_spot(parking_lot:list, vehicle_type:str, parking_pattern:list):

    
    for floor_no in range(len(parking_lot)):
        for slot_no in range(len(parking_lot[0])):
            slot_value = parking_lot[floor_no][slot_no]
            if slot_value==-1 and parking_pattern[slot_no]==vehicle_type:
                return (floor_no, slot_no)

    return (-1, -1)


