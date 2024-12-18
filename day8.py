from collections import defaultdict

grid = []

with open("./inputs/day8.txt", "r") as f:
    for line in f:
        grid.append([char for char in line.strip()])

ROWS = len(grid)
COLS = len(grid[0])

coord_map = defaultdict(set)
for r in range(ROWS):
    for c in range(COLS):
        if grid[r][c] != '.':
            coord_map[grid[r][c]].add((r, c))

vis = set()
vis2 = set()
for freq in coord_map:
    coords = list(coord_map[freq])
    for i in range(len(coords) - 1):
        for j in range(i + 1, len(coords)):
            a1 = coords[i]
            a2 = coords[j]
            vis2.add(a1)
            vis2.add(a2)

            dr = a1[0] - a2[0]
            dc = a1[1] - a2[1]

            newr1, newc1 = a1[0] + dr, a1[1] + dc
            newr2, newc2 = a2[0] - dr, a2[1] - dc
            if 0 <= newr1 < ROWS and 0 <= newc1 < COLS:
                vis.add((newr1, newc1))
            if 0 <= newr2 < ROWS and 0 <= newc2 < COLS:
                vis.add((newr2, newc2))

            while 0 <= newr1 < ROWS and 0 <= newc1 < COLS:
                vis2.add((newr1, newc1))
                newr1 += dr
                newc1 += dc
            while 0 <= newr2 < ROWS and 0 <= newc2 < COLS:
                vis2.add((newr2, newc2))
                newr2 -= dr
                newc2 -= dc

print(len(vis))
print(len(vis2))
