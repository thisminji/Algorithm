#행렬 크기 입력받기
n,m=map(int,input().split())

A=[]
for i in range(n):
    #한 행을 리스트로 받아서 A에 추가
    #2차원 리스트 형태로 행렬 A 완성
    A.append(list(map(int,input().split())))

B=[]
for i in range(n):
    B.append(list(map(int,input().split())))


for i in range(n): #row
    row=[]
    for j in range(m):#col
        row.append(A[i][j]+B[i][j])
    print(*row)