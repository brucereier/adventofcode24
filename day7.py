f = open("./inputs/day7.txt", "r")

final_lines = []  # target num - ordered list of ints

for line in f:
    cur = []
    colon_split = line.split(":")

    cur.append(int(colon_split[0]))
    space_split = colon_split[1].split(" ")
    nums = []
    for x in space_split:
        if x:
            nums.append(int(x))
    cur.append(nums)
    final_lines.append(cur)

total = 0

for entry in final_lines:
    target, vals = entry

    cur_nums = set()
    cur_nums.add(vals[0])

    for num in vals[1:]:
        new_nums = set()
        for prev in cur_nums:
            added = prev + num
            mult = prev * num
            if added == target:
                total += target
                break
            if mult == target:
                total += target
                break

            if added < target:
                new_nums.add(added)

            if mult < target:
                new_nums.add(mult)
        else:
            cur_nums = new_nums
            continue
        break

print(total)
