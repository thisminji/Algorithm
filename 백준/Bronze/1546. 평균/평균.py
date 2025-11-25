# 시험 과목수
n = int(input())
# 점수 리스트
scores = list(map(int, input().split()))
# 최대 점수
max_score = max(scores)
# 새로운 점수 리스트
new_scores = [(score / max_score) * 100 for score in scores]
# 새로운 평균 점수
new_average = sum(new_scores) / n
# 결과 출력
print(new_average)      