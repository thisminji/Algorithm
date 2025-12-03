import sys
from collections import deque

input=sys.stdin.readline

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)

#컴퓨터 개수 N 입력
N = int(input())

# 연결 수 M 입력
M=int(input())

#graph=[[] for _ in range(N+1)] //0신경써서
graph = [[] for _ in range(N+1)]

# M줄 동안 a,b 입력받기 
for _ in range(M):
    a,b=map(int,input().split())
#그래프 무방향 이어주기 graph[a].append(b)/ graoh[b].append(a)
    graph[a].append(b)
    graph[b].append(a)

#visited = [False] * (N+1)
visited=[False]*(N+1)

#실행 bfs(1)
bfs(graph,1,visited)

#visited True인 개수에서 1번 빼고 출력이므로 -1
print(visited.count(True)-1)