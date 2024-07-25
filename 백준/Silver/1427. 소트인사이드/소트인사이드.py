import sys
input = sys.stdin.readline

n = input()
list = []
for i in n :
    list.append(i)
list.sort(reverse=True)
print(''.join(list))