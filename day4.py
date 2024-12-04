f = open("inputs/day4.txt", "r")

grid = []
for line in f:
    cur = []
    for char in line:
        if char in "XMAS":
            cur.append(char)
    grid.append(cur.copy())

ROWS = len(grid)
COLS = len(grid[0])

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

iter_to_char = {
    1: "M",
    2: "A",
    3: "S"
}

total = 0
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] == "X":
            for dr, dc in dirs:
                good = True
                for i in range(1, 4):
                    newr = r + (i * dr)
                    newc = c + (i * dc)  # Fix here
                    if newr < 0 or newr >= ROWS or newc < 0 or newc >= COLS or grid[newr][newc] != iter_to_char[i]:
                        good = False
                        break
                if good:
                    total += 1

corners = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
total2 = 0
for r in range(1, ROWS - 1):
    for c in range(1, COLS - 1):
        if grid[r][c] == "A":
            s = 0
            m = 0
            for dr, dc in corners:
                if grid[r + dr][c + dc] == "M":
                    m += 1
                elif grid[r + dr][c + dc] == "S":
                    s += 1
            if s == 2 and m == 2 and grid[r + 1][c + 1] != grid[r - 1][c - 1]:
                total2 += 1


print(total)
print(total2)
