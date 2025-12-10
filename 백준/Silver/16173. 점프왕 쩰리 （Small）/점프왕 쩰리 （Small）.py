from collections import deque

N = int(input())

board=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]

#이동 가능한 방향은 오른쪽과 아래뿐 위쪽 왼쪽 이동 금지
dx=[1,0] #오른쪽 그대로
dy=[0,1] #그대로 아래

q=deque()
#출발점은 왼쪽 위칸 (0,0)
q.append((0,0))
visited[0][0]=True

answer ="Hing"

while q:
    y,x = q.popleft()
    jump=board[y][x]

    #가장 오른쪽 가장 아래칸  (N,N)? (N-1,N-1) 도달하는 순간 승리 게임종료
    # 먼저 여기가 도착 칸인지 부터 확인
    if jump==-1:
        answer="HaruHaru"
        break

    for dir in range(2):
        nx=x+dx[dir]*jump
        ny=y+dy[dir]*jump

        if 0<=nx <N and 0<=ny <N and not visited[ny][nx]:
            visited[ny][nx]=True
            q.append((ny,nx))
print(answer)
