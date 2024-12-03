from project.band_members.musician import Musician


class Drummer(Musician):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills = []
        self.needed_skills = ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]

