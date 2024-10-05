def draw_cards(*args: tuple[str, str], **kwargs: dict[str]) -> str:
    monster_cards = []
    spell_cards = []

    for card in args:
        card_name, card_type = card
        if card_type == 'monster':
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)

    for card_name, card_type in kwargs.items():
        if card_type == 'monster':
            monster_cards.append(card_name)
        else:
            spell_cards.append(card_name)

    result = ''

    if monster_cards:
        result += f"Monster cards:\n"
        for monster in sorted(monster_cards, reverse=True):
            result += f"  ***{monster}\n"
    if spell_cards:
        result += f"Spell cards:\n"
        for spell in sorted(spell_cards):
            result += f"  $$${spell}\n"

    return result


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))

print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"), ("fireball", "spell"), raigeki="spell", destroy="spell",))

print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))