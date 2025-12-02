import sys
from collections import deque

#내장 입력함수보다 더 빠르게 바꿔줌
input = sys.stdin.readline

# 정점 개수 - N , 간선 개수 - M, 시작 정점 - V
N, M, V = map(int,input().split())

#그래프입력
#숫자가 1부터 시작하니까 정점개수보다 한 개 더 많게 설정
graph = [[] for _ in range (N+1)]

#간선입력 무방향
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#각 정점의 이웃 리스트를 오름차순 정리
for i in range(1,N+1):
    graph[i].sort()

#DFS
visited_dfs=[False]*(N+1)

def dfs(v):
    visited_dfs[v]=True
    print(v,end=' ') #방문순서출력

    for nxt in graph[v]:
        if not visited_dfs[nxt]:
            dfs(nxt)

#BFS
visited_bfs = [False] * (N+1)

def bfs(start):
    # q=deque()
    # q.append(start)

    q = deque([start])
    visited_bfs[start]=True

    while q:
        v=q.popleft()
        print(v,end=' ')

        for nxt in graph[v]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt]=True
                q.append(nxt)

dfs(V)
#줄바꿈
print()
bfs(V)