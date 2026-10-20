from itertools import permutations
def solution(k, dungeons):
    answer=0
    
    for p in permutations(dungeons,len(dungeons)):
        hp=k
        count=0
        
        for d in p:
            if hp>=d[0]:
                hp-=d[1]
                count+=1
        answer=max(answer,count)
        
    return answer