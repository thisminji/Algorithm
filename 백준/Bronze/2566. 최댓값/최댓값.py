#9x9 리스트 형태로 입력 받기
n=[]
for i in range(9):
    n.append(list(map(int,input().split())))

#최대값 구하기
max_value=-1
max_row=0
max_col=0

for i in range(9):
    for j in range(9):
        #최대값 비교 
        if n[i][j]>max_value:
            #최대값이면 max_value 갱신
            max_value=n[i][j]
            #해당 인덱스 저장
            max_row=i+1
            max_col=j+1
            
print(max_value)
print(max_row,max_col)