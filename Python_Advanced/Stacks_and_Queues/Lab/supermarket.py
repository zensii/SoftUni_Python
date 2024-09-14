def collect_names():
    names = []
    while True:
        customer = input()
        if customer == 'End':
            print(f'{len(names)} people remaining.')
            break
        elif customer == 'Paid':
            for name in names:
                print(name)
            names.clear()
        else:
            names.append(customer)

if __name__ == '__main__':
    collect_names()