# 리스트 초기값
pos=[-1]*26
s=input()

# enumerate() (인덱스, 값) 쌍으로 변환
# i는 인덱스 , ch는 문자
for i,ch in enumerate(s):
    # i = 문자열에서의 인덱스
    # idx = 해당 문자가 알파벳에서 몇 번째인지
    # ch - abcd ... idx - 012...
    idx=ord(ch)-ord('a')
    if pos[idx]==-1:
        pos[idx]=i
print(*pos)