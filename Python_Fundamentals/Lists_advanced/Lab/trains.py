def add_passengers(passengers):
    status_wagons[-1] += passengers


def add_at_index(index, passengers):
    status_wagons[index] += passengers


def remove_passengers(index, passengers):
    status_wagons[index] -= passengers


def main(wagons, command):

    while command[0] != 'End':

        if command[0] == 'add':
            add_passengers(int(command[1]))
        elif command[0] == 'insert':
            add_at_index(int(command[1]), int(command[2]))
        elif command[0] == 'leave':
            remove_passengers(int(command[1]),int(command[2]))

        command = input().split()
    return status_wagons


wagons = int(input())
status_wagons = [0]*wagons
command = input().split()
print(main(wagons, command))
