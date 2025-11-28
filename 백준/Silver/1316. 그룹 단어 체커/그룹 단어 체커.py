#그룹단어 개수 세기
n = int(input())

result = 0

for _ in range(n):
    #초기화
    word=input()
    visited = [False]*26
    prev = ''
    is_group = True

    for char in word:
        #이전 글자와 다르면
        if char != prev:
            index=ord(char)-ord('a') #알파벳 인덱스

            if visited[index]: #이미 방문했다면
                is_group=False
                break
            visited[index]=True #방문처리
            prev=char #이전 글자를 갱신
    
    #그룹단어라면
    if is_group:
        result+=1

print(result)


#그룹단어
#글자를 기록해 둘 리스트/배열 필요
#이전글자와 같으면 패스 다르면 새로운 글자면 방문 처리하고 패스
#끝까지 문제 없이 통과하면 그룹단어