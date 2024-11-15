from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150.0
    MIN_STRENGTH_NEEDED = 75

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= self.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak):

        difficulty = peak.calculate_difficulty_level()
        self.strength -= 30 * 1.3 if difficulty == 'Advanced' else 30 * 2.5
        self.conquered_peaks.append(peak.name)