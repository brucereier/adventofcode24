from collections import Counter
f = open("./inputs/day1.txt", "r")

nums1, nums2 = [], []
for line in f:
    nums = line.split()

    nums1.append(int(nums[0]))
    nums2.append(int(nums[1]))

nums1.sort()
nums2.sort()

dist = 0
for i in range(len(nums1)):
    dist += abs(nums1[i] - nums2[i])

print(dist)

##part 2

right_count = Counter(nums2)

sim = 0
for x in nums1:
    if x in right_count:
        sim += x * right_count[x]

print(sim)
