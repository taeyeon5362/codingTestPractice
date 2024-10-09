import sys
input = sys.stdin.readline

T = int(input())
people = []

for _ in range(T):
    name, d, m, y = input().split()
    h = []
    h.append(name)
    h.append(int(d))
    h.append(int(m))
    h.append(int(y))
    people.append(h)

people.sort(key = lambda x : (x[3], x[2],x[1]))

print(people[T-1][0])
print(people[0][0])