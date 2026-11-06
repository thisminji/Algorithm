import math
def solution(num_list):
    if len(num_list)>=11:
        answer=sum(num_list)
    else:
        answer=math.prod(num_list)
    return answer