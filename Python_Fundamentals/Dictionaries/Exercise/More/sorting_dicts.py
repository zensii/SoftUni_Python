data = {
    'B': {'Part Two Interview': 120, 'Math Concept': 250},
    'C': {'Java Advanced': 90, 'Part Two Interview': 0},
    'A': {'Java Advanced': 400, 'Java Web Basics': 280, 'Part Two Interview': 200}
}


sorted_dict = {name: dict(sorted(inner_dict.items(), key=lambda x: x[1], reverse=True)) for name, inner_dict in data.items()}
final_sorted = dict(sorted(sorted_dict.items(), key=lambda x: x[0]))


print(final_sorted)