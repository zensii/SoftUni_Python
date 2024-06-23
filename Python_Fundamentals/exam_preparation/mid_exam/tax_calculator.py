def validate_vehicle(vehicle_type):
    valid_typs = ['family', 'heavyDuty', 'sports']
    if vehicle_type not in valid_typs:
        return False
    return True


def calculate_years_discount(vehicle_type, years):
    year_discounts = {'family': 5,
                      'heavyDuty': 8,
                      'sports': 9
                      }
    discount = year_discounts[vehicle_type] * years
    return discount


def calculate_kilometers_extra(vehicle_type, kilometers):
    km_ranges = {'family': 3000,
                 'heavyDuty': 9000,
                 'sports': 2000
                 }
    km_discounts = {'family': 12,
                    'heavyDuty': 14,
                    'sports': 18
                    }
    discount = kilometers // km_ranges[vehicle_type] * km_discounts[vehicle_type]

    return discount


def provide_initial_tax(vehicle_type):
    initial_taxes = {'family': 50,
                     'heavyDuty': 80,
                     'sports': 100
                     }
    initial_tax = initial_taxes[vehicle_type]
    return initial_tax


def main():

    total_taxes = 0
    vehicles = input().split('>>')

    for vehicle in vehicles:
        vehicle_type, years, kilometers = vehicle.split()
        years = int(years)
        kilometers = int(kilometers)

        if validate_vehicle(vehicle_type):

            tax = (provide_initial_tax(vehicle_type) - calculate_years_discount(vehicle_type, years) +
                   calculate_kilometers_extra(vehicle_type, kilometers))

            total_taxes += tax

            print(f'A {vehicle_type} car will pay {tax:.2f} euros in taxes.')

        else:
            print('Invalid car type.')

    print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')


if __name__ == '__main__':
    main()
