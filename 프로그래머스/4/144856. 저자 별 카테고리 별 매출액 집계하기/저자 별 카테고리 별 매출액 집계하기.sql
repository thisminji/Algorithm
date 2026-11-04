-- 코드를 입력하세요

select A.author_id, C.AUTHOR_NAME, A.category, sum(A.PRICE*B.SALES) AS TOTAL_SALES
from BOOK A, BOOK_SALES B, AUTHOR C
where A.BOOK_ID=B.BOOK_ID
AND A.AUTHOR_ID=C.AUTHOR_ID
AND SALES_DATE LIKE '2022-01%'
group by A.category, A.author_id
order by A.AUTHOR_ID ASC, A.CATEGORY DESC