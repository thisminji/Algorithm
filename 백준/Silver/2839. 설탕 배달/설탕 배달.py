#상근이 설탕 정확하게 N킬로그램 배달 
#봉지는 3킬로그램 봉지와 5킬로 그램 봉지 존재
#최대한 적은 봉지 -> 5킬로

n=int(input())

ans = -1

# range(시작, 끝, step)
#n을 5로 나눈 몫부터 0까지 내려가는 숫자를 의미함
# 5kg 봉지를 최대한 많이 쓰는 경우부터 0개까지 고려해야함 (6kg -> 3kg 2개 가능)
for five in range(n//5,-1,-1):
    rest=n-5*five
    if rest%3==0:
        ans = five+rest//3
        break
print(ans)


