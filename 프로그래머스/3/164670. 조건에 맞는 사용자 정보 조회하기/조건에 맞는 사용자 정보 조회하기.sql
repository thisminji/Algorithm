-- 코드를 입력하세요
SELECT A.WRITER_ID, B.NICKNAME, concat(B.CITY,' ',B.STREET_ADDRESS1,' ',B.STREET_ADDRESS2) AS '전체주소', concat(substring(B.TLNO,1,3),'-',substring(B.TLNO,4,4),'-',substring(B.TLNO,8,4)) AS '전화번호'
from USED_GOODS_BOARD A, USED_GOODS_USER B
where A.WRITER_ID=B.USER_ID
group by A.WRITER_ID
having count(*)>=3
order by B.USER_ID DESC