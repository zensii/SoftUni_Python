import re
string = input()
regex = r'([=\/])([A-Z][A-Za-z]{2,})\1'
travel_points = [match[1] for match in re.findall(regex, string)]
print(f"Destinations: {', '.join(travel_points)}")
print(f'Travel Points: {sum(len(point) for point in travel_points)}')
