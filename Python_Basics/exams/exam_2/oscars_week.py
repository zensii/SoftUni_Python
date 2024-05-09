movie_name = input()
hall = input()
tickets = int(input())
p = 0

ticket_types = ['normal', 'luxury', 'ultra luxury']
movies = ['A Star Is Born', 'Bohemian Rhapsody', 'Green Book', 'The Favourite']
prices = [7.5, 10.5, 13.5, 7.35, 9.45, 12.75, 8.15, 10.25, 13.25, 8.75, 11.55, 13.95]

for movie in movies:
    for ticket in ticket_types:
        price = prices[p]
        p += 1
        if movie == movie_name and hall == ticket:
            print(f'{movie} -> {price * tickets:.2f} lv.')
