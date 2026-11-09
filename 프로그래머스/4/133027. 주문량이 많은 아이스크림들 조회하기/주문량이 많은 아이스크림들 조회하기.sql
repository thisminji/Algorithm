-- 코드를 입력하세요
select A.FLAVOR
from FIRST_HALF A,(
    SELECT FLAVOR, sum(TOTAL_ORDER) AS TOTAL
from JULY 
group by FLAVOR) B
where A.FLAVOR=B.FLAVOR
order by A.TOTAL_ORDER + B.TOTAL DESC
limit 3

