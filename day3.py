input = ""
with open("./inputs/day3.txt", "r") as f:
    input = f.read()

start = 0
str_len = len(input)
cur = 0
enabled = True

while start < str_len:

    find = input.find("mul", start)
    if find == -1:
        break

    i = find + 3
    if i >= str_len or input[i] != "(":
        start = find + 1
        continue
    i += 1

    num1 = 0
    while i < str_len and input[i].isdigit():
        num1 = num1 * 10 + int(input[i])
        i += 1

    if i >= str_len or input[i] != ",":
        start = find + 1
        continue
    i += 1

    num2 = 0
    while i < str_len and input[i].isdigit():
        num2 = num2 * 10 + int(input[i])
        i += 1

    if i >= str_len or input[i] != ")":
        start = find + 1
        continue
    i += 1
    
    last_dont = input.rfind("don't()", 0, find)
    last_do = input.rfind("do()", 0, find)
    if last_do >= last_dont:
        cur += (num1 * num2)

    start = i

print(cur)




