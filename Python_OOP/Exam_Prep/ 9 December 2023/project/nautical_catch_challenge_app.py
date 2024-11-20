from typing import List

from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.divers.base_diver import BaseDiver
from project.fish.base_fish import BaseFish
from project.fish.deep_sea_fish import DeepSeaFish
from project.fish.predatory_fish import PredatoryFish


class NauticalCatchChallengeApp:
    ALLOWED_DIVER_TYPES = {"FreeDiver":FreeDiver, "ScubaDiver": ScubaDiver}
    ALLOWED_FISH = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: List[BaseDiver] = []
        self.fish_list: List[BaseFish] = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.ALLOWED_DIVER_TYPES:
            return f"{diver_type} is not allowed in our competition."

        if diver_name in [diver.name for diver in self.divers]:
            return f"{diver_name} is already a participant."


        new_diver = self.ALLOWED_DIVER_TYPES[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.ALLOWED_FISH:
            return f"{fish_type} is forbidden for chasing in our competition."

        if fish_name in [fish.name for fish in self.fish_list]:
            return f"{fish_name} is already permitted."


        new_fish = self.ALLOWED_FISH[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.get_diver(diver_name)
        fish = self.get_fish(fish_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."


        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."
        else:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        with_health_issues = [diver for diver in self.divers if diver.has_health_issue is True]
        for diver in with_health_issues:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(with_health_issues)}"

    def diver_catch_report(self, diver_name: str):
        diver = self.get_diver(diver_name)
        return f"**{diver_name} Catch Report**\n" + "\n".join(fish.fish_details() for fish in diver.catch)

    def competition_statistics(self):

        result = "**Nautical Catch Challenge Statistics**"
        for diver in sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name)):
            result += '\n' + diver.__str__() if not diver.has_health_issue else ''
        return result

    def get_diver(self, name):
        return next((diver for diver in self.divers if diver.name == name), None)

    def get_fish(self, name):
        return next((fish for fish in self.fish_list if fish.name == name), None)