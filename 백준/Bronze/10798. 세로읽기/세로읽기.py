alpa = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(alpa[i]):
            print(alpa[i][j], end='')