from project.band_members.musician import Musician


class Singer(Musician):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.needed_skills = ["sing high pitch notes", "sing low pitch notes"]