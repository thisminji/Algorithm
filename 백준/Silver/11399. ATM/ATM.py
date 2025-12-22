# 각 사람의 인출시간 P[i]가 있을 때, 총 대기시간 합을 최소 = 짧게 걸리는 사람을 앞에 세워야 함
n=int(input())
p=list(map(int,input().split()))

#list.sort() mutable / sorted() immutable
p.sort()

prefix=0
ans=0

for t in p:
    prefix=prefix+t
    ans=ans+prefix
print(ans)
