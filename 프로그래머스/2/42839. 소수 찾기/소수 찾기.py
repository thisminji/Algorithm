from itertools import permutations

def solution(numbers):
    nums=set()
    
    for i in range(len(numbers)):
        for j in permutations(numbers,i+1):
            num=int(''.join(j))
            nums.add(num)
    
    answer=0
    for num in nums:
        if num<2:
            continue
        for i in range(2,num):
            if num%i==0:
                break
        else:
            answer+=1
    return answer