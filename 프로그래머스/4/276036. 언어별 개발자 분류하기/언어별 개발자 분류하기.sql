SELECT (CASE
    when
        MAX(CASE WHEN A.CATEGORY = 'Front End' THEN 1
            ELSE 0 END)
            AND
        MAX(CASE WHEN A.NAME = 'Python' THEN 1
            ELSE 0 END) then 'A'
        
    when MAX(CASE WHEN A.NAME='C#' then 1
            else 0 end) then 'B'
    when MAX(CASE WHEN A.CATEGORY = 'Front End' THEN 1 
             ELSE 0 END) then 'C'
        END) AS GRADE, B.ID, B.EMAIL
FROM SKILLCODES A, DEVELOPERS B
WHERE (A.CODE & B.SKILL_CODE) > 0 
group by ID
HAVING GRADE IS NOT NULL
order by GRADE, ID