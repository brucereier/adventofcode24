def is_valid(nums):
    is_dec = nums[1] < nums[0]
    for i in range(len(nums) - 1):
        if is_dec:
            if nums[i + 1] >= nums[i] or nums[i + 1] <= nums[i] - 4:
                return False
        else:
            if nums[i + 1] <= nums[i] or nums[i + 1] >= nums[i] + 4:
                return False
    return True

def is_tolerant(nums):
    if is_valid(nums):
        return True
    
    for i in range(len(nums)):
        new_nums = nums[:i] + nums[i+1:]
        if is_valid(new_nums):
            return True
    return False

good_lines = 0
tolerable_lines = 0
with open("./inputs/day2.txt", "r") as f:
    for line in f:
        nums = [int(x) for x in line.split()]
        if is_tolerant(nums):
            tolerable_lines += 1
        if is_valid(nums):
            good_lines += 1

print(good_lines)
print(tolerable_lines)
