from typing import List
from project.battleships.base_battleship import BaseBattleship
from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:

    def __init__(self):
        self.zones: List[BaseZone] = []
        self.ships: List[BaseBattleship] = []


    def add_zone(self, zone_type: str, zone_code: str):

        if zone_type not in map(lambda x: x.__class__.__name__, self.zones):
            if zone_type == 'RoyalZone':
                self.zones.append(RoyalZone(zone_code))
            elif zone_type == 'PirateZone':
                self.zones.append(PirateZone(zone_code))
            else:
                raise Exception("Invalid zone type!")
            return f"A zone of type {zone_type} was successfully added."
        raise Exception("Zone already exists!")


    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):

        if ship_type in ['RoyalBattleship', 'PirateBattleship']:
            self.ships.append(RoyalBattleship(name, health, hit_strength) if ship_type == 'RoyalBattleship' else
                              PirateBattleship(name, health, hit_strength))
            return f"A new {ship_type} was successfully added."

        raise Exception(f"{ship_type} is an invalid type of ship!")


    @staticmethod
    def add_ship_to_zone(zone: BaseZone, ship: BaseBattleship):

        if not zone.volume > 0:
            return f"Zone {zone.code} does not allow more participants!"
        if not ship.health > 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"
        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if zone.__class__.__name__.startswith('Royal'):
            if ship.__class__.__name__.startswith('Royal'):
                ship.is_attacking = True
        elif zone.__class__.__name__.startswith('Pirate'):
            if ship.__class__.__name__.startswith('Pirate'):
                ship.is_attacking = True
        else:
            ship.is_attacking = False

        ship.is_available = False
        zone.ships.append(ship)
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):

        if not ship_name in [ship.name for ship in self.ships]:
            return "No ship with this name!"
        ship_inst = [ship for ship in self.ships if ship.name == ship_name][0]
        if not ship_inst.is_available:
            return f"The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(ship_inst)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone: BaseZone):

        attackers = [ship for ship in zone.ships if ship.is_attacking and ship.__class__.__name__[:5] == zone.__class__.__name__[:5]]
        defenders = [ship for ship in zone.ships if not ship.is_attacking and ship.__class__.__name__[:5] != zone.__class__.__name__[:5]]

        if len(attackers) == 0 or len(defenders) == 0:
            return "Not enough participants. The battle is canceled."

        attacker = sorted(attackers, key=lambda x: (-x.hit_strength, x.name))[0]
        defender = sorted(defenders, key=lambda x: (-x.health, x.name))[0]

        attacker.attack()
        defender.take_damage(attacker)

        if defender.health <= 0:
            self.ships.remove(defender)
            zone.ships.remove(defender)
            return f"{defender.name} lost the battle and was sunk."

        if attacker.ammunition <= 0:
            self.ships.remove(attacker)
            zone.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."


    def get_statistics(self):
        available_ships = [ship for ship in self.ships if ship.is_available]
        available_ships_str = ', '.join(ship.name for ship in available_ships) if available_ships else ''

        zones_info = '\n'.join(zone.zone_info() for zone in sorted(self.zones, key=lambda z: z.code))

        result = f"Available Battleships: {len(available_ships)}\n"
        result += f"#{available_ships_str}#\n" if available_ships else ''
        result += (f"***Zones Statistics:***\n"
                   f"Total Zones: {len(self.zones)}"
                   f"\n{zones_info}")
        return result.strip()
