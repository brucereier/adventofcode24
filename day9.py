inp = open("./inputs/day9.txt", "r")

txt = ""
for line in inp:
    txt = line.strip()

print(txt)

ind = 0
files = []
for i in range(0, len(txt), 2):
    for j in range(int(txt[i])):
        files.append(ind)
    if i + 1 != len(txt):
        for k in range(int(txt[i + 1])):
            files.append(-1)
    ind += 1

l = 0
r = len(files) - 1

while l < r:
    while files[l] != -1 and l < r:
        l += 1
    while files[r] == -1 and r > l:
        r -= 1

    files[l], files[r] = files[r], files[l]

total = 0
for i, num in enumerate(files):
    if num != -1:
        total += i * num
print(total)
