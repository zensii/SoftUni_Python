from datetime import datetime, timedelta
from collections import deque


def collect_products():
    products = deque()
    while True:
        product = input()
        if product == 'End':
            break
        products.append(product)
    return products


def check_free_robots(time):
    freed_robots= []
    current_busy = busy_robots.copy()
    for robot in current_busy:
        if time - robot[2] >= timedelta(seconds=robot[1]):
            freed_robots.append(robot)
            busy_robots.remove(robot)
    return freed_robots


robots = deque([[robot_name, int(speed)] for robot_info in input().split(';') for robot_name, speed in [robot_info.split('-')]])
time = datetime.strptime(input(), "%H:%M:%S")
tact = timedelta(seconds=1)

for robot in robots:
    robot.append(time)

products = collect_products()
free_robots = robots.copy()
busy_robots = deque()

while products:

    time += tact

    if busy_robots:
        freed_robots = check_free_robots(time)
        for robot in freed_robots:
            free_robots.insert(robots.index(robot), robot)

    if free_robots and products:

        print(f'{free_robots[0][0]} - {products.popleft()} [{time.time()}]')
        free_robots[0][2] = time
        busy_robots.append(free_robots.popleft())

    else:
        products.rotate(-1)

