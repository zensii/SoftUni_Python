from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {"Guitarist": Guitarist, "Drummer": Drummer, "Singer": Singer}

    def __init__(self):
        self.bands = []
        self.musicians = []
        self.concerts = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        if [m for m in self.musicians if m.name == name]:
            raise Exception(f"{name} is already a musician!")
        new_musician = self.VALID_MUSICIANS[musician_type](name, age)
        self.musicians.append(new_musician)
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        if [b for b in self.bands if b.name == name]:
            raise Exception(f"{name} band is already created!")
        new_band = Band(name)
        self.bands.append(new_band)
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        booked_concert = [c for c in self.concerts if c.place == place]
        if booked_concert:
            raise Exception(f"{place} is already registered for {booked_concert[0].genre} concert!")
        new_concert = Concert(genre, audience, ticket_price, expenses, place)
        self.concerts.append(new_concert)
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician = [m for m in self.musicians if m.name == musician_name]
        if not musician:
            raise Exception(f"{musician_name} isn't a musician!")

        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")

        band[0].members.append(musician[0])
        return f"{musician_name} was added to {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band = [b for b in self.bands if b.name == band_name]
        if not band:
            raise Exception(f"{band_name} isn't a band!")
        band_member = [m for m in band[0].members if m.name == musician_name]
        if not band_member:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band[0].members.remove(band_member[0])
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        needed_musicians = ['Singer', 'Drummer', 'Guitarist']
        concert_requirements = {'Rock': {'play the drums with drumsticks', 'sing high pitch notes', 'play rock'},
                                'Metal': {'play the drums with drumsticks', 'sing low pitch notes', 'play metal'},
                                'Jazz': {'play the drums with drum brushes', 'sing high pitch notes', 'sing low pitch notes', 'play jazz'}}

        band = [b for b in self.bands if b.name == band_name][0]
        concert = [c for c in self.concerts if c.place == concert_place][0]
        musicians = band.members
        genre = concert.genre
        band_skills = []

        for musician in musicians:
            musician_type = musician.__class__.__name__
            if musician_type in needed_musicians:
                needed_musicians.remove(musician_type)
            band_skills.extend(musician.skills)
        if needed_musicians:
            raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        missing_skills = concert_requirements[genre].difference(band_skills)
        if missing_skills:
            raise Exception(f"The {band_name} band is not ready to play at the concert!")

        total_profit = (concert.audience * concert.ticket_price) - concert.expenses
        return f"{band_name} gained {total_profit:.2f}$ from the {concert.genre} concert in {concert_place}."

