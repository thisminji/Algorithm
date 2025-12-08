import sys
from collections import deque

input = sys.stdin.readline

#상하좌우
dx=[0,0, -1,1]
dy=[-1,1,0,0]

# (시작x, 시작y, 배추밭, 방문배열, 가로 M, 세로 N)
def bfs(start_x,start_y,field,visited,M,N):
    q=deque()
    q.append((start_x,start_y))
    # field = [[0]*M for _ in range(N)]
    #우리가 만든 리스트의 구조가 행 열 구조라서 
    visited[start_y][start_x]=True

    while q:
        x,y = q.popleft()

        #현재 (x,y)에서 상하좌우로 이동
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i] 

            #밭 범위 안에 위치
            if 0<=nx <M and 0<=ny <N:
                #배추가 있고 방문 안했으면 
                if field[ny][nx]==1 and not visited[ny][nx]:
                    visited[ny][nx]=True  
                    q.append((nx,ny))

#테스트 케이스 수 입력
T=int(input().strip())

#배추밭 가로길이  세로길이 배추가 심어져있는 위치의 개수  M N K 입력
for _ in range(T):
    M,N,K=map(int,input().split())

    #가로가 M이고 세로가 N
    #배추 밭 방문 배열 초기화 
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

#     field = [
#     [0, 0, 0, ... M개]   # 0번째 행 (y=0)
#     [0, 0, 0, ... M개]   # 1번째 행 (y=1)
#     [0, 0, 0, ... M개]   # 2번째 행 (y=2)
#     ...
#     # 총 N개 행
# ]    

    for _ in range(K):  
        #k줄에는 배추의 위치(x,y) 입력
        x,y=map(int, input().split())
        # field = [[0]*M for _ in range(N)]
        #우리가 만든 리스트의 구조가 행 열 구조라서 
        field[y][x]=1

    worm_count=0

    for y in range(N): #행
        for x in range(M): #열
            #배추 있고 방문 안했으면 
            if field[y][x]==1 and not visited[y][x]:
                bfs(x,y,field,visited,M,N)
                worm_count+=1
    
    print(worm_count)