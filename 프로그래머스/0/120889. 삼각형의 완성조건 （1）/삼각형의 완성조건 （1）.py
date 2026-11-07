def solution(sides):
    answer = 0
    if sum(sides)-max(sides)>max(sides):
        return 1 
    else: 
        return 2