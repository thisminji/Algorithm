-- 코드를 입력하세요
select A.category, A.price, A.PRODUCT_NAME
from food_product A,
(
    SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE
    from FOOD_PRODUCT
    group by CATEGORY
) B
where A.CATEGORY=B.CATEGORY
AND A.price=B.MAX_PRICE
AND A.category IN ('과자','국','김치', '식용유')
order by A.price desc

