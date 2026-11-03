def solution(l, r):
    answer = []
    
    for i in range(1,2**len(str(r))):
        num=int(bin(i)[2:].replace('1','5'))
        if l<=num<=r:
            answer.append(num)    
    return answer if answer else [-1]