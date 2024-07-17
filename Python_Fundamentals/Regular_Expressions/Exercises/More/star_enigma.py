import re


def decode(coded_messages):

    decoded = []
    for coded_message in coded_messages:
        key = len(re.findall(r'[star]', coded_message, re.I))
        decoded_message = ''.join([chr((ord(char) - key)) for char in coded_message])
        decoded.append(decoded_message)
    return decoded


def calculate_damage(decoded_message):

    battle_report = {}

    for decoded_message in decoded_message:

        key = r'[^@\-!:>]*@([a-zA-Z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)[^@\-!:>]*'
        target = re.findall(key, decoded_message)
        if target:
            planet_name, population, att_type, solders = target[0]
            battle_report.setdefault(att_type, []).append(planet_name)

    return battle_report


def main():
    coded_messages = []

    messages = int(input())
    for message in range(messages):
        coded_messages.append(input())
    decoded_messages = decode(coded_messages)
    battle_report = calculate_damage(decoded_messages)

    attacked_planets = sorted(battle_report.get('A', []))
    destroyed_planets = sorted(battle_report.get('D', []))

    print(f"Attacked planets: {len(attacked_planets)}")
    for planet in attacked_planets:
        print(f'-> {planet}')
    print(f"Destroyed planets: {len(destroyed_planets)}")
    for planet in destroyed_planets:
        print(f'-> {planet}')


if __name__ == '__main__':
    main()
