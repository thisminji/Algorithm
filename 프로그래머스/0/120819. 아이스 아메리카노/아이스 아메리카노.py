def solution(money):
    cup=money//5500
    save=money%5500    
    return [cup,save]