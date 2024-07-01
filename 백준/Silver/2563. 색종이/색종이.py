n = int(input())
array = [[0]*100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())
    # x : x ~ x+10
    # y : y ~ y+10
    for i in range(y, y+10):
        idx_y = i
        for j in range(x, x+10):
            idx_x = j
            if array[idx_y][idx_x] == 0:
                array[idx_y][idx_x] = 1
            else:
                pass

sum_array = 0
for i in range(100):
    sum_array += sum(array[i])
print(sum_array)