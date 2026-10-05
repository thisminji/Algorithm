-- 코드를 작성해주세요
select b.SCORE, a.EMP_NO, a.EMP_NAME, a.position, a.email
from HR_EMPLOYEES A,(
    select emp_no, sum(score) as score
from HR_GRADE 
where year=2022
group by emp_no)
b
where a.EMP_NO = b.EMP_NO
order by b.score desc
limit 1