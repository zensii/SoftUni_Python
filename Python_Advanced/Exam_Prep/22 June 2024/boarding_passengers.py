def boarding_passengers(ship_capacity: int, *groups: tuple[int, str]) -> str:
    classes = {}
    to_board = list(groups)
    for group in groups:
        ppl_in_group, ticket_class = group[0], group[1]
        if ship_capacity >= ppl_in_group:
            classes[ticket_class] = classes.setdefault(ticket_class, 0) + ppl_in_group
            ship_capacity -= ppl_in_group
            del to_board[0]
    result = 'Boarding details by benefit plan:\n'

    for class_group, passengers in dict(sorted(classes.items(), key= lambda x: (-x[1], x))).items():
        result += f"## {class_group}: {passengers} guests\n"

    if len(to_board) == 0:
        result += "All passengers are successfully boarded!"
    else:
        if ship_capacity == 0:
            result += "Boarding unsuccessful. Cruise ship at full capacity."
        else:
            result += f"Partial boarding completed. Available capacity: {ship_capacity}."

    return result

print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))

print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'), (10, 'Gold')))

print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'), (20, 'Diamond')))