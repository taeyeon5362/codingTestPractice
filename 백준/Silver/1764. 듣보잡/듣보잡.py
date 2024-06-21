import sys
input = sys.stdin.readline

N, M = map(int, input().split())
no_listen = set()
no_watch= set()

for i in range(N) :
    no_listen.add(input().strip())

for i in range(M) :
    no_watch.add(input().strip())

print(len(no_listen & no_watch))
for i in sorted(no_listen & no_watch) :
    print(i)
