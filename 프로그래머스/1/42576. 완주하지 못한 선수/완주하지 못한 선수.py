def solution(participant, completion):
    count={}
    
    for i in participant:
        count[i]=count.get(i,0)+1
    for i in completion:
        count[i]=count.get(i,0)-1
    for i in count:
        if count[i]==1:
            return i