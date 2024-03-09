T = int(input())
people = list(map(int, input().split()))
time = []
people.sort()
time_num = 0

for i in range(T) :
    time_num += people[i]
    time.append(time_num)
print(sum(time))