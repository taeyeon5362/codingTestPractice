x = int(input())
bar = [64, 32, 16, 8, 4, 2, 1]
result = 0

for i in range(len(bar)):
    if x >= bar[i]:
        result += 1
        x -= bar[i]

    if x == 0:
        break

print(result)