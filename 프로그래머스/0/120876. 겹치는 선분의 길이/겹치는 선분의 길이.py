def solution(lines):
    count={}
    for start, end in lines:
        for i in range(start,end):
            count[i]=count.get(i,0)+1
    return sum(1 for v in count.values() if v>=2)