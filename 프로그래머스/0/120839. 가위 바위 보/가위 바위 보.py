def solution(rsp):
    rule = {'2': '0', '0': '5', '5': '2'}
    answer = ''
    for i in rsp:
        answer+=rule[i]
    return answer