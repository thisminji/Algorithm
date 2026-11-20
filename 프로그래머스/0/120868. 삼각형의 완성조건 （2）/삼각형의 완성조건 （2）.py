def solution(sides):
    answer = 0
    for x in range(max(sides)-min(sides)+1,sum(sides)):
        if (max(sides) - min(sides) < x  and x<= max(sides)) or (max(sides) < x  and x< sum(sides)):
            answer+=1
    return answer