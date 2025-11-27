#공백으로 구분 된 숫자들을 리스트
# list(int(input().split())) 에러
base = [1,1,2,2,2,8]
s = list(map(int, input().split()))

for i in range(len(base)): #6
   print(base[i]-s[i], end=' ')


# base = [1,1,2,2,2,8]
# s = list(map(int, input().split()))
# #result를 빈 리스트로 선언
# result = []
# for i in range(len(base)): #6
# #그래서 append로 추가
# #만약 result에 [0,0,0,0,0,0] 초기화하면
# #인덱스 에러 발생
#    result.append(base[i]-s[i])
# print(*result)