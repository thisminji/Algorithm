def solution(clothes):
    count={}
    
    for i in clothes:
        type=i[1]
        count[type]=count.get(type,0)+1
    answer=1
    for i in count.values():
        answer=answer*(i+1)
    return answer-1