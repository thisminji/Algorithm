def solution(participant, completion):
    mp = {}
    for name in participant:
        mp[name]=mp.get(name,0)+1
        
    for name in completion:
        mp[name]-=1
        
        # mp.items() - 딕셔너리에 들어있는 키 값 쌍을 전부 꺼내줌
    for name, cnt in mp.items():
        if cnt==1:
            return name