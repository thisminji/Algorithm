#무방향 그래프에서 연결요소 개수 구하는 프로그램
#첫쨰줄에 정점의 개수 N 간선의 개수 M

import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, graph, visited):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt]=True
                q.append(nxt)

N, M = map(int,input().split())

#정점 개수만큼 빈 리스트 만들기
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)
cnt = 0

for i in range(1,N+1):
    if not visited[i]:
        bfs(i,graph,visited)
        cnt+=1

print(cnt)