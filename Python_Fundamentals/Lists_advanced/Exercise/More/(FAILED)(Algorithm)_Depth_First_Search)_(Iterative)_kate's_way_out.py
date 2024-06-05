def iterative_dfs(maze, start):
    n = len(maze)
    m = len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    stack = [(start[0], start[1], 1)]  # (x, y, moves)
    max_moves = 0

    while stack:
        x, y, moves = stack.pop()

        # If out of bounds or hit a wall, continue
        if x < 0 or x >= n or y < 0 or y >= m or maze[x][y] == '#' or maze[x][y] == 'v':
            continue

        # If at the edge of the maze, update max_moves
        if x == 0 or x == n-1 or y == 0 or y == m-1:
            max_moves = max(max_moves, moves)

        maze[x][y] = 'v'  # Mark as visited

        for dx, dy in directions:
            stack.append((x + dx, y + dy, moves + 1))

    return max_moves

# Read input
n = int(input())
maze = [list(input().strip()) for _ in range(n)]

# Find Kate's starting position
start = None
for i in range(n):
    for j in range(len(maze[i])):
        if maze[i][j] == 'k':
            start = (i, j)
            break
    if start:
        break

# Call the iterative DFS function
result = iterative_dfs(maze, start)

if result > 1:
    print(f"Kate got out in {result} moves")
else:
    print("Kate cannot get out")
