#정사각형 섬 가로세로대각선 이동 가능


#입력이 여러 번 들어옴: (w, h)가 0 0 나오면 종료
# 그 지점부터 BFS/DFS로 8방향으로 퍼지면서 같은 섬을 전부 방문 처리
# 섬 개수 +1
# 두번째 즐 부터 h개 줄에는 지도 주어짐 (1-땅 0-바다)
#입력의 마지막 줄에는 00 주어짐

import sys
input = sys.stdin.readline

# ↖ ↑ ↗ ← → ↙ ↓ ↘
dx=[-1,0,1,-1,1,-1,0,1]
dy=[-1,-1,-1,0,0,1,1,1]

while True:
    w,h = map(int, input().split())
    if w==0 and h==0:
        break

    grid=[list(map(int,input().split())) for _ in range(h)]
    visited=[[False] * w for _ in range(h)]

    cnt = 0

    for y in range(h):
        for x in range(w):
            if grid[y][x]==1 and not visited[y][x]:
                cnt+=1
                stack=[(x,y)]
                visited[y][x]=True

                while stack: 
                    cx,cy=stack.pop()
                    #한 칸에서 갈 수 있는 방향이 8개라서 
                    for k in range(8):
                        nx=cx+dx[k]
                        ny=cy+dy[k]
                        if 0<=nx <w and 0<=ny <h:
                            if grid[ny][nx]==1 and not visited[ny][nx]:
                                visited[ny][nx]=True
                                stack.append((nx,ny))
    print(cnt)
