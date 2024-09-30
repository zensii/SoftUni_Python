def accommodate(*guests, **rooms):
    sorted_rooms = dict(sorted(rooms.items(), key=lambda x: (x[1], x[0].split('_')[1])))
    accommodations = []
    guests_to_accommodate = sum(guests)
    for group in guests:

        for room, cap in sorted_rooms.items():

            if cap >= group:
                guests_to_accommodate -= group
                accommodations.append((room.split('_')[1], group))
                sorted_rooms[room] = 0
                del rooms[room]
                break

    result = ''

    if accommodations:
        result += f"A total of {len(accommodations)} accommodations were completed!\n"

        for accommodation in sorted(accommodations, key=lambda x: x[0]):
            result += f"<Room {accommodation[0]} accommodates {accommodation[1]} guests>\n"
    else:
        result += "No accommodations were completed!\n"

    if guests_to_accommodate:
        result += f"Guests with no accommodation: {guests_to_accommodate}\n"

    if rooms:
        result += f"Empty rooms: {len(rooms)}"

    return result

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))

print(accommodate(10, 9, 8, room_307=6, room_802=5))

print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))