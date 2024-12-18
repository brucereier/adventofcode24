from collections import deque

f = open("./inputs/day18.txt", "r")
grid = [["."] * 71 for _ in range(71)]
ROWS = len(grid)
COLS = len(grid[0])

ct = 0
for line in f:
    if ct == 1024:
        break
    text = line.strip()
    nums = text.split(",")
    grid[int(nums[0])][int(nums[1])] = "#"
    ct += 1

q = deque([(0, 0, 0)])
grid[0][0] = "v"
print(grid)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while q:
    r, c, dist = q.popleft()

    if r == 70 and c == 70:
        print(dist)
        break

    for dr, dc in dirs:
        newr = r + dr
        newc = c + dc

        if 0 <= newr < ROWS and 0 <= newc < COLS and grid[newr][newc] == ".":
            q.append((newr, newc, dist + 1))
            grid[newr][newc] = "v"

else:
    print("No path found.")
