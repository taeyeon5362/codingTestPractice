import sys
input = sys.stdin.readline

N = int(input())
bring = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

count_dict = {}
for card in bring:
    if card in count_dict:
        count_dict[card] += 1
    else:
        count_dict[card] = 1

result = []
for query in num:
    result.append(count_dict.get(query, 0))

print(' '.join(map(str, result)))
