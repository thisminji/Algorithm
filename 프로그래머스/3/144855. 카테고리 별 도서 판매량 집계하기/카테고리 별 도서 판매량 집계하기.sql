SELECT A.category, Sum(B.SALES) AS TOTAL_SALES
From BOOK A, BOOK_SALES B
where A.BOOK_ID=B.BOOK_ID AND B.SALES_DATE LIKE '2022-01-%'
group by A.category
order by A.category