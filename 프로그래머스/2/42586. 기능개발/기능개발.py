from collections import deque

def solution(progresses,speeds):
    days=deque()

    for p,s in zip(progresses,speeds):
        remain=100-p
        d=(remain+s-1)//s
        days.append(d)
    result=[]

    while days:
        depoly_day=days[0]
        cnt=0
        while days and days[0]<=depoly_day:
            days.popleft()
            cnt+=1
        result.append(cnt)
    return result