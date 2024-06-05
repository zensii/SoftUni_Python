n = int(input())
maze = [list(input().strip()) for _ in range(n)]

start = None
for i in range(n):
    for j in range(len(maze[i])): # can also directly put 6 as it is a constant
        if maze[i][j] == 'k':
            start = (i, j)
            break
    if start:
        break

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right


# this is the Recursive Depth-First Search algorythm
def dfs(x, y, moves):
    if x < 0 or x >= n or y < 0 or y >= len(maze[0]) or maze[x][y] == '#' or maze[x][y] == 'v':
        return 0
    if x == 0 or x == n - 1 or y == 0 or y == len(maze[0]) - 1:
        return moves

    maze[x][y] = 'v'  # Mark as visited
    max_moves = 0
    for dx, dy in directions:
        max_moves = max(max_moves, dfs(x + dx, y + dy, moves + 1))
    maze[x][y] = ' '  # Unmark as visited

    return max_moves


result = dfs(start[0], start[1], 1)
if result > 0:
    print(f"Kate got out in {result} moves")
else:
    print("Kate cannot get out")
