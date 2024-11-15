from typing import List

from project.climbers.arctic_climber import ArcticClimber
from project.climbers.base_climber import BaseClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    conquered_peaks = set() # keep track of unique names

    def __init__(self):
        self.climbers: List[BaseClimber] = []
        self.peaks: List[BasePeak] = []

    @staticmethod
    def _get_climber_type(climber_type):
        return {'ArcticClimber': ArcticClimber, 'SummitClimber': SummitClimber}.get(climber_type, None)


    def _get_climber_by_name(self, climber_name):
        return next((c for c in self.climbers if c.name == climber_name), None)


    def register_climber(self, climber_type: str, climber_name: str):

        if self._get_climber_type(climber_type) is None:
            return f"{climber_type} doesn't exist in our register."
        if self._get_climber_by_name(climber_name) is not None:
            return f"{climber_name} has been already registered."
        new_climber = self._get_climber_type(climber_type)(climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."


    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):

        valid_peak = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}.get(peak_type, None)
        if valid_peak is None:
            return f"{peak_type} is an unknown type of peak."
        new_peak = valid_peak(peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."


    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):

        climber = next((c for c in self.climbers if c.name == climber_name), None)
        peak = next((p for p in self.peaks if p.name == peak_name), None)
        needed_gear = set(peak.get_recommended_gear())
        missing_gear = needed_gear.difference(gear)

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted(list(missing_gear)))}."


    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._get_climber_by_name(climber_name)
        peak = next((p for p in self.peaks if p.name == peak_name), None)

        if not climber:
            return f"Climber {climber_name} is not registered yet."
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."
        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        if not climber.can_climb():
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

        self.conquered_peaks.add(peak_name)
        climber.climb(peak)
        return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."


    def get_statistics (self):
        successful_climbers = sorted([c for c in self.climbers if c.conquered_peaks], key=lambda c: (-len(c.conquered_peaks), c.name))

        return f"Total climbed peaks: {len(self.conquered_peaks)}\n**Climber's statistics:**\n" + '\n'.join(str(c) for c in successful_climbers)


# Create an instance of SummitQuestManagerApp
climbing_app = SummitQuestManagerApp()

# Register climbers
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Bob"))
print(climbing_app.register_climber("ExtremeClimber", "Dave"))
print(climbing_app.register_climber("ArcticClimber", "Charlie"))
print(climbing_app.register_climber("ArcticClimber", "Alice"))
print(climbing_app.register_climber("SummitClimber", "Eve"))
print(climbing_app.register_climber("SummitClimber", "Frank"))

# Add peaks to the wish list
print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))

# Prepare climbers for climbing
print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))

# Perform climbing
print(climbing_app.perform_climbing("Alice", "MountEverest"))
print(climbing_app.perform_climbing("Bob", "K2"))
print(climbing_app.perform_climbing("Kelly", "Denali"))
print(climbing_app.perform_climbing("Alice", "K2"))
print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
print(climbing_app.perform_climbing("Eve", "MountEverest"))
print(climbing_app.perform_climbing("Charlie", "MountEverest"))
print(climbing_app.perform_climbing("Frank", "K2"))
print(climbing_app.perform_climbing("Frank", "Denali"))
print(climbing_app.perform_climbing("Frank", "MountEverest"))

# Get statistics
print(climbing_app.get_statistics())
