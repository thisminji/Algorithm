def solution(hp):    
    answer=hp//5
    rest=hp%5
    answer+=rest//3
    rest%=3
    answer+=rest
    
    return answer