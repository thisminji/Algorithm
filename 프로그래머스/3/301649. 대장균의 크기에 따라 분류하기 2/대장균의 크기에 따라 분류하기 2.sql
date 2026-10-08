-- 코드를 작성해주세요
select ID,
case 
       when GROUP_NUM=1 then 'CRITICAL'
       when GROUP_NUM=2 then 'HIGH'
       when GROUP_NUM=3 then 'MEDIUM'
       when GROUP_NUM=4 then 'LOW'
END AS COLONY_NAME
from (
            select ID, 
                   SIZE_OF_COLONY,
                   NTILE(4) over (order by SIZE_OF_COLONY DESC ) AS GROUP_NUM
            from ECOLI_DATA
    ) A
ORDER BY ID