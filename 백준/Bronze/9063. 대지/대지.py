import sys
input = sys.stdin.readline

T = int(input())
a_list = []
b_list = []
for _ in range(T) :
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
a_list.sort()
b_list.sort()
print((a_list[T-1] - a_list[0])*(b_list[T-1] - b_list[0]))