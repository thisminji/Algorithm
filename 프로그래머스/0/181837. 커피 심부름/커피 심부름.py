def solution(order):
    answer = 0
    option1=["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]
    option2=["icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"]
    
    for i in order:
        if i in option1:
            answer+=4500
        else:
            answer+=5000
    return answer