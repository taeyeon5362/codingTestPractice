import sys
input = sys.stdin.readline

T = int(input())
for i in range(T) :
        n, m = map(int, input().split())
        answer = (m-n+1)*(n+m)//2
        print('Scenario #{}:'.format(i+1))
        print(answer)
        print("")