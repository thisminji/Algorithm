#숫자 뒤집기
# 문자열로 바꾸고 [::-1]
a,b = input().split()
a=int(a[::-1])
b=int(b[::-1])
print(max(a,b))