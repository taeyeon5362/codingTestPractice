import sys
input = sys.stdin.readline

n = int(input().rstrip())

for i in range(n) :
    answer = ''
    s = input().rstrip()
    for j in s :
        if j == 'Z' :
            answer += 'A'
        else :
            answer += chr(ord(j)+1)
    print('String #{}'.format(i+1))
    print(answer, '\n')