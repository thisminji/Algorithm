# 1. 100×100 배열을 0으로 초기화
# 2. 색종이 개수 N개
# 3. N번 반복하면서 색종이의 (x,y) 좌표 입력
# 4. (x,y)부터 10x10 크기의 영역을 1
# 5. 최종적으로 1로 채워진 칸의 개수 출력

paper = [[0]*100 for _ in range(100)]

n=int(input())

for _ in range(n):
    x,y=map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j]=1

count=0
for i in range(100):
    for j in range(100):
        if paper[i][j]==1:
            count+=1

print(count)