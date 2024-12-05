from collections import defaultdict, deque


def topological_sort(nodes, before_map):
    # Calculate in-degrees for each node
    in_degree = {node: 0 for node in nodes}
    for node in nodes:
        for dependent in before_map[node]:
            if dependent in nodes:  # Only consider dependencies within this update
                in_degree[dependent] += 1

    # Start with nodes that have no dependencies (in-degree 0)
    queue = deque([node for node in nodes if in_degree[node] == 0])
    sorted_order = []

    while queue:
        current = queue.popleft()
        sorted_order.append(current)

        for dependent in before_map[current]:
            if dependent in nodes:  # Only consider dependencies within this update
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    queue.append(dependent)

    return sorted_order


# Read the input file
f = open("inputs/day5.txt", "r")

before_map = defaultdict(set)
correct_total = 0
incorrect_updates = []

# Parse the input
for line in f:
    if "|" in line:
        num1, num2 = line.split("|")
        num2 = num2[:len(num2) - 1]
        before_map[int(num1)].add(int(num2))
    elif "," in line:
        nums = line.split(",")
        nums[-1] = nums[-1][:len(nums[-1]) - 1]
        int_nums = [int(num) for num in nums]

        vis = set()
        good = True
        for x in int_nums:
            for ref in before_map[x]:
                if ref in vis:
                    good = False
                    break
            vis.add(x)
            if not good:
                break

        if good:
            correct_total += int_nums[len(int_nums) // 2]
        else:
            incorrect_updates.append(int_nums)

# Part 1 output
print("Part 1:", correct_total)

# Process incorrectly ordered updates for Part 2
incorrect_total = 0
for update in incorrect_updates:
    # Get the correct order using topological sorting
    sorted_update = topological_sort(update, before_map)

    # Find the middle page number and add it to the total
    incorrect_total += sorted_update[len(sorted_update) // 2]

# Part 2 output
print("Part 2:", incorrect_total)
