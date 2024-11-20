from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DEFAULT_OXYGEN = 120
    def __init__(self, name: str):
        super().__init__(name, self.DEFAULT_OXYGEN)

    def miss(self, time_to_catch):
        if self.oxygen_level >= time_to_catch:
            self.oxygen_level -= time_to_catch * 0.6
            self.oxygen_level = round(self.oxygen_level)
        else:
            self.oxygen_level = 0
        if self.oxygen_level == 0:
            self.has_health_issue = True

    def renew_oxy(self):
        self.oxygen_level = self.DEFAULT_OXYGEN

