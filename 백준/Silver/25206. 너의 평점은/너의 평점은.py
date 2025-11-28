#전공평점 3.3이상인지 판별하는 프로그램
#전공평점: 학점*과목평점의 합 / 이수한 총 학점

#20줄 입력받기 
#과목명, 학점, 과목평점 순서로 입력
#ex) 자료구조 3 4.0

#과목평점 테이블
grade_table={
    "A+":4.5,
    "A0":4.0,
    "B+":3.5,
    "B0":3.0,
    "C+":2.5,
    "C0":2.0,
    "D+":1.5,
    "D0":1.0,
    "F":0.0
}

total_score=0.0
total_credit=0.0

for _ in range(20):
    subject,credit,grade=input().split()
    credit=float(credit)

    if grade=="P":
        continue
    
    #입력으로 받은 grade를 grade_table에서 학점을 찾아서 계산
    total_score+=credit*grade_table[grade]
    total_credit+=credit
print(total_score/total_credit)
# print(f"{값:형식}")
# print(f"{total_score/total_credit:.6f}")