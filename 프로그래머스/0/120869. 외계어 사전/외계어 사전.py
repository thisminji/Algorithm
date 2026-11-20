def solution(spell, dic):
    answer = 2
    for i in dic:
        if len(spell)==len(i):
            cnt=0
            for j in spell:
                if i.count(j)==1:
                    cnt+=1
            if cnt==len(i):
                  answer=1
    return answer