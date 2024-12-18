inp = open("./inputs/day9.txt", "r")

# Read input
txt = ""
for line in inp:
    txt = line.strip()

print("Disk Map:", txt)

# Parse disk map
ind = 0
files = []
for i in range(0, len(txt), 2):
    for j in range(int(txt[i])):
        files.append(ind)
    if i + 1 < len(txt):
        for k in range(int(txt[i + 1])):
            files.append(-1)
    ind += 1

print("Initial Files:")
print(files)

# Get unique file IDs (descending order)
file_ids = sorted(set(files) - {-1}, reverse=True)

# Compact files by moving whole files
for file_id in file_ids:
    # Find file's current position range
    start = files.index(file_id)
    # Reverse lookup for last occurrence
    end = len(files) - 1 - files[::-1].index(file_id)
    file_size = end - start + 1

    # Find leftmost free space of sufficient size
    for i in range(len(files) - file_size + 1):
        if files[i:i + file_size] == [-1] * file_size:
            # Move the file
            files[i:i + file_size] = [file_id] * file_size
            files[start:end + 1] = [-1] * file_size
            break

print("Compacted Files:")
print(files)

# Calculate the checksum
total = sum(i * num for i, num in enumerate(files) if num != -1)
print("Checksum:", total)
