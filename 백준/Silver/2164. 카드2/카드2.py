import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
list = deque(range(1, n + 1))

while len(list) > 1:
    list.popleft()  # 제일 위의 카드를 버림
    list.append(list.popleft())  # 제일 위의 카드를 제일 아래로 옮김

print(list[0])