import sys
input = sys.stdin.readline

N = int(input())
record = []
answer = []

for i in range(N) :
    file = list(input())
    if i == 0 :
        answer.append(file)
    
    record.append(file)

for i in range(N-1) :
    for j in range(len(record[0])) :
        if record[i][j] == record[i+1][j] :
            continue
        else :
            answer[0][j] = '?'


print(''.join(answer[0]))