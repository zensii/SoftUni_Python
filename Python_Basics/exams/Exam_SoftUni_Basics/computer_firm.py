PC_models = int(input())
total_sales = 0
sum_ratings = 0

for pc_model in range(1, PC_models + 1):
    sales_ratings = input()

    current_rating = int(sales_ratings[-1:])

    possible_sales = int(sales_ratings) // 10

    if current_rating == 2:
        total_sales += 0
    elif current_rating == 3:
        total_sales += int(possible_sales) / 2
    elif current_rating == 4:
        total_sales += int(possible_sales) * 0.7
    elif current_rating == 5:
        total_sales += int(possible_sales) * 0.85
    elif current_rating == 6:
        total_sales += int(possible_sales)

    sum_ratings += int(current_rating)

print(f'{total_sales:.2f}')
print(f'{sum_ratings/PC_models:.2f}')

