import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dic = {}

for i in range(1, N+1) :
    a = input().rstrip()
    dic[i] = a
    dic[a] = i
  

for i in range(M) :
    po = input().rstrip()
    if po.isdigit() :
        print(dic[int(po)])
    else :
        print(dic[po])