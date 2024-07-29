
n, m = map(int, input().split())
board = []
result = []

for _ in range(n) :
    board.append(input())

for i in range(n-7) :
    for j in range(m-7) :
        a = 0
        b = 0
        for k in range(i, i+8) :
            for l in range(j, j+8) :
                if (k + l) % 2 == 0 :
                    if board[k][l] != 'B' :
                        a += 1
                    if board[k][l] != 'W' :
                        b += 1
                else :
                    if board[k][l] != 'W' :
                        a += 1
                    if board[k][l] != 'B' :
                        b += 1
        result.append(a)
        result.append(b)
print(min(result))