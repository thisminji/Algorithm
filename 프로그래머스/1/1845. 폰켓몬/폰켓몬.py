def solution(nums):
    n=len(nums)
    limit=n//2
    
    mp={}
    
    for x in nums:
        mp[x]=mp.get(x,0)+1
        # 딕셔너리는 중복 불허용 
        # 딕셔너리에서 len()은 키 종류 개수 카운트
    kinds=len(mp)

    return min(limit,kinds)