def solution(n):
    answer = [[0]*n for _ in range(n)]
    x,y=0,0
    d=0
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    
    for num in range(1,n*n+1):
        answer[y][x]=num
        nx=x+dx[d]
        ny=y+dy[d]
        
        if 0<=nx<n and 0<=ny<n and answer[ny][nx]==0:
            x=nx
            y=ny
        else:
            d=(d+1)%4
            x=x+dx[d]
            y=y+dy[d]
            
            
    return answer