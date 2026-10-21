import math

def solution(progresses, speeds):
    day = []

    for i in range(len(progresses)):
        day.append(math.ceil((100 - progresses[i]) / speeds[i]))
     
    answer=[]
    count=1
    start=day[0]
    
    for i in range(1,len(day)):
        if day[i]<=start:
            count+=1
        else:
            answer.append(count)
            count=1
            start=day[i]
    answer.append(count)
    return answer