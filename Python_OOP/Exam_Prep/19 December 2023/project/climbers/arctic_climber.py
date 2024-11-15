from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200.0
    MIN_STRENGTH_NEEDED = 100
    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= self.MIN_STRENGTH_NEEDED

    def climb(self, peak: BasePeak):

        difficulty = peak.calculate_difficulty_level()
        self.strength -= 20 * 2 if difficulty == 'Extreme' else 20 * 1.5
        self.conquered_peaks.append(peak.name)

