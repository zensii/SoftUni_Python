number_of_movies = int(input())

highest_rating = float('-infinity')
highest_rating_movie = ''
lowest_rating = float('infinity')
lowest_rating_movie = ''
sum_ratings = 0

for movie in range(1, number_of_movies+1):
    name = input()
    rating = float(input())
    if rating > highest_rating:
        highest_rating = rating
        highest_rating_movie = name
    elif rating < lowest_rating:
        lowest_rating = rating
        lowest_rating_movie = name
    sum_ratings += rating
print(f'{highest_rating_movie} is with highest rating: {highest_rating:.1f}')
print(f'{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}')
print(f'Average rating: {sum_ratings/number_of_movies:.1f}')
