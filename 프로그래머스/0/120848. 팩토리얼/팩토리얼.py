def solution(n):
    answer = 0
    factorial=1
    for i in range(1,11):
        factorial*=i
        if factorial<=n:
            answer=i
    return answer