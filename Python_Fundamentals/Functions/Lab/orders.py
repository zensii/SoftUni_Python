prices = {
    'coffee': 1.50,
    'water': 1.00,
    'coke': 1.40,
    'snacks': 2.00,
}


def order(product, quantity):
    return prices[product] * quantity


product = input()
quantity = int(input())

print(f'{order(product, quantity):.2f}')