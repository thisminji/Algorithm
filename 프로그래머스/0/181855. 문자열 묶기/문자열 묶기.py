def solution(strArr):
    answer = 0
    count={}
    for i in strArr:
        count[len(i)]=count.get(len(i),0)+1
    return max(count.values())