def solution(citations):
    for i in range(len(citations)+1):
        count=0
        for j in citations:
            if j>=i:
                count+=1
        if count>=i:
            answer=i
    return answer