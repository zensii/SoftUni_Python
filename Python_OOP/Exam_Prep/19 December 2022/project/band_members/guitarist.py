from project.band_members.musician import Musician


class Guitarist(Musician):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.needed_skills = ["play metal", "play rock", "play jazz"]
