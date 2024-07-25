import sys
input = sys.stdin.readline

n = int(input())
s_list = list(map(int, input().split()))
m = int(input())
new_list = list(map(int, input().split()))

dic = {}
for i in range(n):
    dic[s_list[i]] = i

for i in range(m) :
  if new_list[i] not in dic :
      print(0, end=' ')
  else :
      print(1, end=' ')