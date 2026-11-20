def solution(board):
    answer = 0
    danger=[[0]*len(board[0]) for _ in range(len(board))]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==1:
                for di in range(-1,2):
                    for dj in range(-1,2):
                        ni=i+di
                        nj=j+dj
                        
                        if 0<=ni<len(board) and 0<=nj<len(board[0]):
                            danger[ni][nj]=1
    for i in danger:
        answer+=i.count(0)
    
    return answer