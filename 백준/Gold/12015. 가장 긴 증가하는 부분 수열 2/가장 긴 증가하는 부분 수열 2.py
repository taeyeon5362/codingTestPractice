import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
num_list = [*map(int, input().split())]

lis = [num_list[0]]

for i in num_list :
    if lis[-1] < i :
        lis.append(i)
    else :
        idx = bisect_left(lis, i)
        lis[idx] = i

print(len(lis))