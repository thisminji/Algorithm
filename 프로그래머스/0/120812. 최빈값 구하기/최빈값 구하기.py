def solution(array):
    count=[0]*1000
    
    for i in array:
        count[i]+=1
    if count.count(max(count))>1:
        return -1
    return count.index(max(count))