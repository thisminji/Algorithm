n=int(input())
s=input()
# 문자열 한 글자씩 확인 = for ch in s
print(sum(int(ch)for ch in s))