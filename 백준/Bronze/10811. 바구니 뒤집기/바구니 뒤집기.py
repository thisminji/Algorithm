# N : 바구니 개수 M : 뒤집기 횟수
n,m =map(int,input().split())
# 바구니 세팅
arr = list(range(1,1+n))
for _ in range(m):
    i,j = map(int,input().split())
    arr[i-1:j]=reversed(arr[i-1:j])
 # arr은 리스트로 출력됌
print(*arr)
