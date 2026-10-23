-- 코드를 입력하세요
SELECT sales_date, product_id, user_id,sales_amount
from ONLINE_SALE
where sales_date LIKE '2022-03%'

UNION ALL

SELECT sales_date, product_id, null as user_id,sales_amount
from OFFLINE_SALE
where sales_date LIKE '2022-03%'

order by sales_date ASC, product_id ASC, user_id ASC