from collections import defaultdict


def read_grid(filename):
    with open(filename) as f:
        grid = [list(line.strip('\n')) for line in f]
    # Clean grid to only contain valid chars
    for r in range(len(grid)):
        grid[r] = [c for c in grid[r] if c in "v^<>#."]
    return grid


def find_guard(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] in "v^<>":
                return r, c, grid[r][c]
    return None, None, None


dirs = {"v": (1, 0), "^": (-1, 0), "<": (0, -1), ">": (0, 1)}
next_dir = {"v": "<", "<": "^", "^": ">", ">": "v"}


def simulate(grid):
    R, C = len(grid), len(grid[0])
    guardr, guardc, cur = find_guard(grid)
    visited_states = set()
    visited_positions = set()
    while True:
        state = (guardr, guardc, cur)
        if state in visited_states:
            return visited_positions, True
        visited_states.add(state)
        visited_positions.add((guardr, guardc))

        dr, dc = dirs[cur]
        nr, nc = guardr + dr, guardc + dc
        # Out of bounds => done
        if nr < 0 or nr >= R or nc < 0 or nc >= C:
            return visited_positions, False
        if grid[nr][nc] == "#":
            cur = next_dir[cur]
            continue
        guardr, guardc = nr, nc


def main():
    grid = read_grid("inputs/day6.txt")
    start_r, start_c, _ = find_guard(grid)
    visited_positions, _ = simulate(grid)

    loop_count = 0
    for (r, c) in visited_positions:
        # Skip starting pos and existing obstacles
        if (r, c) == (start_r, start_c) or grid[r][c] == "#":
            continue
        # Temporarily place obstruction
        original = grid[r][c]
        grid[r][c] = "#"
        _, loops = simulate(grid)
        if loops:
            loop_count += 1
        # Restore
        grid[r][c] = original

    print("Distinct positions visited (part1):", len(visited_positions))
    print("Positions causing loops (part2):", loop_count)


if __name__ == "__main__":
    main()
