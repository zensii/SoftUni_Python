from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return Hotel(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people):
        for room in self.rooms:
            if room.number ==  room_number:
                room.take_room(people)
                if room.is_taken:
                    self.guests += people
                break

    def free_room(self, room_number: int):
        for room in self.rooms:
            if room.number == room_number:
                leaving = room.guests
                room.free_room()
                if not room.is_taken:
                    self.guests -= leaving
                break

    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n"
                f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}")



hotel = Hotel.from_stars(5)
room = Room(1, 3)
hotel.add_room(room)
hotel.take_room(1, 3)
hotel.free_room(1)


print(hotel.status())
