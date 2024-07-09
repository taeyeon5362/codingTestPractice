import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

T = int(input())  # 컴퓨터의 수 (노드의 수)
c = int(input())  # 연결된 쌍의 수 (간선의 수)

graph = [[] for _ in range(T+1)]

for _ in range(c):
    n, m = map(int, input().split())
    graph[n].append(m)
    graph[m].append(n)

visited = [False] * (T + 1)

# 1번 컴퓨터에서 시작
dfs(graph, 1, visited)

# 1번 컴퓨터를 제외한 감염된 컴퓨터 수를 계산
infected_count = sum(visited) - 1
print(infected_count)