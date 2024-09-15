from collections import deque

fuel = 0
stations_qty = int(input())
stations = deque()
current = 0
start_station = 0

for _ in range(stations_qty):
    stations.append(tuple(map(int, input().split())))

while current < len(stations):
    if stations[current][0] + fuel >= stations[current][1]:
        fuel += stations[current][0] - stations[current][1]
        current += 1
    else:
        stations.append(stations.popleft())
        current = 0
        start_station += 1
        fuel = 0

print(start_station)