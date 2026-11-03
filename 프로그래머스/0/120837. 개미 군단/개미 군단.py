def solution(hp):
    answer = 0
    
    answer=hp//5
    rest=hp%5
    answer=answer+rest//3
    rest=rest%3
    answer=answer+rest//1
    
    return answer