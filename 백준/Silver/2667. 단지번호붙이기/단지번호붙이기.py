import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

#sys.stdin.readline은 줄 끝의 \n 같이 읽어오는 문제가 발생해서 stip()사용해야함
#strip() - 문자열의 앞뒤에 붙은 공백 제거 
graph = [list(map(int,input().strip())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]

#코딩에서
# x = 행 (row)  → 위/아래 움직임
# y = 열 (col)  → 왼/오른쪽 움직임

#상하좌우 
#행이 변하는 경우
dx=[-1,1,0,0]
#열이 변하는 경우
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    #시작 집 한 채 카운트
    count=1

    # x, y : 시작점
	# cx, cy : 현재 처리 중인 점 (current x, current y)

    while q:
        #큐에서 꺼낸, 지금 기준이 되는 집 위치
        cx, cy = q.popleft()

        for d in range(4):
            # (cx, cy) : 현재 집
            # (nx, ny) : d방향으로 한 칸 이동한 위치
            nx=cx+dx[d]
            ny=cy+dy[d]

            #nx가 지도 안에 있는 인덱스인지 확인하는 조건
            if 0<=nx < N and 0<=ny <N:
                #이 칸은 집이고 (1) 아직 한 번도 안가본 칸
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append((nx,ny))
                    count+=1
    return count

#각 단지의 집 개수 저장
complex_sizes=[]
for i in range(N):
    for j in range(N):
        if graph[i][j]==1 and not visited[i][j]:
            size = bfs(i,j)
            complex_sizes.append(size)

#오름차순 정렬
complex_sizes.sort()

#출력
print(len(complex_sizes)) #단지수
for s in complex_sizes: #단지 별 집 개수
    print(s)
