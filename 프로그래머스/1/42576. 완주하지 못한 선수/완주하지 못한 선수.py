def solution(participant, completion):
    mp = {}

    # 참가자 이름 개수 세기(+1)
    for name in participant:
        mp[name] = mp.get(name, 0) + 1

    # 완주자 이름 개수 빼기(-1)
    for name in completion:
        mp[name] -= 1

    # 1 남은 사람이 미완주자
    for name, cnt in mp.items():
        if cnt == 1:
            return name