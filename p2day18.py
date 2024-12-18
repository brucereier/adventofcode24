from collections import deque

# Read input and initialize grid
f = open("./inputs/day18.txt", "r")
grid = [["."] * 71 for _ in range(71)]
ROWS, COLS = len(grid), len(grid[0])
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# Parse input and simulate byte corruption
for line in f:
    # Parse the byte coordinates
    text = line.strip()
    x, y = map(int, text.split(","))
    grid[x][y] = "#"

    # Perform BFS to check if a path exists
    q = deque([(0, 0)])
    visited = [[False] * COLS for _ in range(ROWS)]
    visited[0][0] = True

    path_found = False
    while q:
        r, c = q.popleft()

        if r == 70 and c == 70:
            path_found = True
            break

        for dr, dc in dirs:
            newr, newc = r + dr, c + dc
            if (0 <= newr < ROWS and 0 <= newc < COLS and grid[newr][newc] == "." and not visited[newr][newc]):
                q.append((newr, newc))
                visited[newr][newc] = True

    # If no path is found, output the blocking byte and exit
    if not path_found:
        print(f"{x},{y}")
        break
