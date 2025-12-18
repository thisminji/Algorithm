#루트없는 트리 주어짐
# 트리의 루트를 1이라 했을 때 각 노드의 부모 구하는 거

import sys
from collections import deque

#노드의 개수 n

def bfs(start,graph,visited):
    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt]=True
                # 부모 기록해야함
                # v에서 nxt로 처음 이동하는 순간 그 방향을 ‘부모 → 자식’이라고 정한다
                parent[nxt]=v
                q.append(nxt)

n =int(input())

parent = [0]*(n+1)
graph = [[] for _ in range(n+1)]
visited =[False]*(n+1)

# 간선 입력 개수 오류 - 노드가 n개면 간선은 n-1 개 받아야함
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1,graph,visited)

for i in range(2,n+1):
    print(parent[i])

