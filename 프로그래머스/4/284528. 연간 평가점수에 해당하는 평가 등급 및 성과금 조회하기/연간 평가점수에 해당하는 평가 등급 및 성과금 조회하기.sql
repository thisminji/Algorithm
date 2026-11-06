# -- 코드를 작성해주세요
select A.EMP_NO, A.EMP_NAME, B.GRADE, (
    case when B.GRADE='S' then SAL*0.2
    when B.GRADE='A' then SAL*0.15
    when B.GRADE='B'then SAL*0.1
    else 0
    end
)AS BONUS
from HR_EMPLOYEES A, (select EMP_NO, AVG(SCORE) AS AVG_SCORE,
( case when AVG(SCORE)>=96 then 'S'
 when AVG(SCORE)>=90 then 'A'
 when AVG(SCORE)>=80 then 'B'
 else 'C'
 end) AS GRADE
from HR_GRADE 
group by EMP_NO) B
where A.EMP_NO=B.EMP_NO
order by A.EMP_NO ASC



