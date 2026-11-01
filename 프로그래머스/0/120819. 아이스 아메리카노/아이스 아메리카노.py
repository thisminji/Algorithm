def solution(money):
    answer = []
    cup=money//5500
    save=money%5500
    answer.append(cup)
    answer.append(save)
    
    return answer