import sys
input = sys.stdin.readline

T = int(input())
num_list = []
for i in range(T) :
    a = int(input())
    num_list.append(a)
num_list.sort(reverse=True)
for i in num_list :
    print(i)