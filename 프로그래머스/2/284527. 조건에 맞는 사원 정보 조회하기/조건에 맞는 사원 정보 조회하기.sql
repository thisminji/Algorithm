-- 코드를 작성해주세요
select a.score, b.EMP_NO, b.EMP_NAME, b.POSITION,b.EMAIL
from HR_EMPLOYEES b, 
(
select c.EMP_NO, sum(c.score) AS score
FROM HR_GRADE c
where c.YEAR=2022
group by c.emp_no) a
where b.emp_no=a.emp_no
order by score desc 
limit 1