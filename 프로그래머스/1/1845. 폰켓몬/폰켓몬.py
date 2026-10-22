def solution(nums):
    n=len(nums)//2
    count={}
    
    for i in nums:
        count[i]=count.get(i,0)+1    
    answer = min(len(count),n)
    return answer