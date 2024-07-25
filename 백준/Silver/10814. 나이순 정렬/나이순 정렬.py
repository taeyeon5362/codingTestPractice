import sys
input = sys.stdin.readline

N = int(input())
list = []

for _ in range(N) :
    a, b = input().split()
    list.append([int(a),b])
  
list.sort(key = lambda x : x[0])
for i in list :
    print(i[0], i[1])